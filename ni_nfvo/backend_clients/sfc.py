# -*- coding: utf-8 -*-
import requests
import uuid
import netaddr
import logging

from ni_nfvo.config import cfg
from ni_nfvo.backend_clients.utils import openstack_client as client
from ni_nfvo.backend_clients.utils import zun_client
from ni_nfvo.database import db

from flask import abort

log = logging.getLogger(__name__)

vnf_cfg = cfg["openstack_client"]["vnf"]
data_net_id = client.get_net_id_from_name(vnf_cfg["data_net_name"])
base_url = client.base_urls["network"]


def _abort_if_sfc_conflict(sfcr_ids, vnf_ids_lists):
    all_sfcs = db.get_all_sfcs()
    used_sfcr_ids = []
    used_vnf_ids = []
    for sfc in all_sfcs:
        used_sfcr_ids.extend(sfc.sfcr_ids)
        for vnf_ids in sfc.vnf_instance_ids:
            used_vnf_ids.extend(vnf_ids)

    for sfcr_id in sfcr_ids:
        if sfcr_id in used_sfcr_ids:
            error_message = "sfcr %s is already used" %(sfcr_id)
            log.error(error_message)
            abort(400, error_message)

    for vnf_ids in vnf_ids_lists:
        for vnf_id in vnf_ids:
            if vnf_id in used_vnf_ids:
                error_message = "vnf %s is already used" % (vnf_id)
                log.error(error_message)
                abort(400, error_message)


def is_vnf_active(vnf_id):
    if zun_client.is_container(vnf_id):
        vnf = zun_client.client.containers.get(vnf_id)
        return vnf.status == "Running"
    else:
        base_url = client.base_urls["compute"]
        url = "/servers/{}".format(vnf_id)
        headers = {'X-Auth-Token': client.get_token()}

        req = requests.get("{}{}".format(base_url, url),
                            headers=headers)

        if req.status_code == 200:
            return (req.json()["server"]["status"] == 'ACTIVE')
        else:
            abort(req.status_code, req.text)

def _abort_if_vnf_not_active(vnf_ids_lists):
    for vnf_ids in vnf_ids_lists:
        for vnf_id in vnf_ids:
            if not is_vnf_active(vnf_id):
                abort(400, "vnf %s is not ACTIVE" %(vnf_id))


def create_sfc(fc_prefix, sfcr_ids, vnf_ids_lists, is_symmetric=False):
    if len(vnf_ids_lists) == 0:
        error_message = "vnf list is empty"
        log.error(error_message)
        abort(404, error_message)

    if len(sfcr_ids) == 0:
        error_message = "sfcr_ids is empty"
        log.error(error_message)
        abort(404, error_message)

    _abort_if_sfc_conflict(sfcr_ids, vnf_ids_lists)
    _abort_if_vnf_not_active(vnf_ids_lists)

    port_ids_list = []
    for vnf_ids in vnf_ids_lists:
        port_ids = [_get_data_port(vnf_id) for vnf_id in vnf_ids]
        port_ids_list.append(port_ids)

    if fc_prefix:
        postfix_name = "{}_{}".format(fc_prefix, str(uuid.uuid4()))
    else:
        postfix_name = "{}".format(str(uuid.uuid4()))

    port_pairs_ids_list = _create_port_pairs(postfix_name, port_ids_list)
    pp_group_ids = _create_port_pair_groups(postfix_name, port_pairs_ids_list)
    p_chain_id = _create_port_chain(postfix_name, pp_group_ids, sfcr_ids, is_symmetric)

    return p_chain_id

def _get_data_port(vnf_instance_id):
    url = "v2.0/ports?device_id={}".format(vnf_instance_id)
    req = requests.get("{}{}".format(base_url, url),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        log.error(req.text)
        abort(req.status_code, req.text)

    req = req.json()

    for port in req["ports"]:
        if port["network_id"] == data_net_id:
            return port["id"]

    error_message = "no data port for vnf id: {}".format(vnf_instance_id)
    log.error(error_message)
    abort(400, error_message)


def _ip_prefix_conflict(first_ip_prefix, second_ip_prefix):
    if first_ip_prefix is None or second_ip_prefix is None:
        return True
    first_ipset = netaddr.IPSet([first_ip_prefix])
    second_ipset = netaddr.IPSet([second_ip_prefix])
    return bool(first_ipset & second_ipset)


def _port_range_conflict( first_port_range_min, first_port_range_max,
        second_port_range_min, second_port_range_max ):
    first_conflict = True
    second_conflict = True
    if (
        first_port_range_min is not None and
        second_port_range_max is not None
    ):
        first_conflict = first_port_range_min <= second_port_range_max
    if (
        first_port_range_max is not None and
        second_port_range_min is not None
    ):
        second_conflict = second_port_range_min <= first_port_range_max
    return first_conflict & second_conflict


def _protocol_conflict(first_protocol, second_protocol):
    if first_protocol is None or second_protocol is None:
        return True
    return first_protocol == second_protocol


def _sfcr_conflict(sfcr1, sfcr2):
    return all([
        _protocol_conflict(sfcr1.proto, sfcr2.proto),
        _ip_prefix_conflict(sfcr1.src_ip_prefix, sfcr2.src_ip_prefix),
        _ip_prefix_conflict(sfcr1.dst_ip_prefix, sfcr2.dst_ip_prefix),
        _port_range_conflict(
            sfcr1.src_port_min,
            sfcr1.src_port_max,
            sfcr2.src_port_min,
            sfcr2.src_port_max
        ),
        _port_range_conflict(
            sfcr1.dst_port_min,
            sfcr1.dst_port_max,
            sfcr2.dst_port_min,
            sfcr2.dst_port_max
        )
    ])


def create_flow_classifier(sfcr_spec):
    url = "/v2.0/sfc/flow_classifiers"

    # Originally, Openstack allow more relaxed (and flexible) conflict check,
    # but this can cause later conflict when creating sfc.
    # Thus we enforce a strict flow-classifier check
    # at the begining to prevent conflict.
    for sfcr in db.get_all_sfcrs():
        # sfcr_spec contain all needed infor for sfcr_confict checking
        if _sfcr_conflict(sfcr, sfcr_spec):
            error_message = "sfcr conflict with sfcr: %s" %(sfcr.id)
            log.error(error_message)
            abort(400, error_message)

    body = dict()
    # logical_source_port is required
    body["logical_source_port"] = _get_data_port(sfcr_spec.source_client)

    if sfcr_spec.destination_client is not None:
        body["logical_destination_port"] = _get_data_port(sfcr_spec.destination_client)

    if sfcr_spec.src_ip_prefix is not None:
        body["source_ip_prefix"] = sfcr_spec.src_ip_prefix
    if sfcr_spec.dst_ip_prefix is not None:
        body["destination_ip_prefix"] = sfcr_spec.dst_ip_prefix
    if sfcr_spec.src_port_min is not None:
        body["source_port_range_min"] = sfcr_spec.src_port_min
    if sfcr_spec.src_port_max is not None:
        body["source_port_range_max"] = sfcr_spec.src_port_max
    if sfcr_spec.dst_port_min is not None:
        body["destination_port_range_min"] = sfcr_spec.dst_port_min
    if sfcr_spec.dst_port_max is not None:
        body["destination_port_range_max"] = sfcr_spec.dst_port_max
    if sfcr_spec.proto is not None:
        body["protocol"] = sfcr_spec.proto

    body = {"flow_classifier": body}

    req = requests.post("{}{}".format(base_url, url),
        json=body,
        headers={'X-Auth-Token': client.get_token()})

    if req.status_code == 201:
        return req.json()["flow_classifier"]["id"]
    else:
        log.error(req.text)
        abort(req.status_code, req.text)


def _create_port_pairs(postfix_name, port_ids_list, allow_existing_pp=False):
    # create port_pairs from ports. Use the same port for ingress and egress

    req = requests.get("{}{}".format(base_url, "/v2.0/sfc/port_pairs"),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        log.error(req.text)
        abort(req.status_code, req.text)
    req = req.json()
    existing_port_pairs = req["port_pairs"]

    port_pairs_list = []
    for i, port_ids in enumerate(port_ids_list):
        port_pairs = []
        for j, port_id in enumerate(port_ids):
            to_create_new = True

            if (allow_existing_pp):
                for port_pair in existing_port_pairs:
                    if port_pair["ingress"] == port_id and port_pair["egress"] == port_id:
                        port_pairs.append(port_pair["id"])
                        to_create_new = False
                        break

            if to_create_new:
                body = {
                            "port_pair": {
                                "ingress": port_id,
                                "egress": port_id,
                                "name": "pp_{}{}_{}".format(i, j, postfix_name),
                            }
                        }

                req = requests.post("{}{}".format(base_url, "/v2.0/sfc/port_pairs"),
                    json=body,
                    headers={'X-Auth-Token': client.get_token()})

                if req.status_code == 201:
                    port_pairs.append(req.json()["port_pair"]["id"])
                else:
                    log.error(req.text)
                    abort(req.status_code, req.text)

        port_pairs_list.append(port_pairs)

    return port_pairs_list

def _create_port_pair_groups(postfix_name, port_pairs_list):
    # create port pair group for each port_pairs
    port_pair_groups = []
    for i, port_pairs in enumerate(port_pairs_list):
        body = {
                    "port_pair_group": {
                        "port_pairs": port_pairs,
                        "name": "ppg_{}_{}".format(i, postfix_name),
                    }
                }

        req = requests.post("{}{}".format(base_url, "/v2.0/sfc/port_pair_groups"),
            json=body,
            headers={'X-Auth-Token': client.get_token()})

        if req.status_code == 201:
            port_pair_groups.append(req.json()["port_pair_group"]["id"])
        else:
            log.error(req.text)
            abort(req.status_code, req.text)

    return port_pair_groups

def _create_port_chain(postfix_name, port_pair_groups, flow_classifiers, is_symmetric):
    body = {
                "port_chain": {
                    "flow_classifiers": flow_classifiers,
                    "port_pair_groups": port_pair_groups,
                    "name": "pc_{}".format(postfix_name),
                    "chain_parameters": {
                        "symmetric": True if is_symmetric else False
                    }
                }
            }

    req = requests.post("{}{}".format(base_url, "/v2.0/sfc/port_chains"),
        json=body,
        headers={'X-Auth-Token': client.get_token()})

    if req.status_code == 201:
        return req.json()["port_chain"]["id"]
    else:
        log.error(req.text)
        abort(req.status_code, req.text)


def update_sfc(sfc_id, sfcr_ids=None, vnf_ids_lists=None):
    sfc = db.get_sfc(sfc_id)
    if sfc is None:
        error_message = "sfc_id: {} not found".format(sfc_id)
        log.error(error_message)
        abort(404, error_message)

    _abort_if_vnf_not_active(vnf_ids_lists)

    if vnf_ids_lists:
        _update_sfc_vnf_ids(sfc, vnf_ids_lists, update_db=False)
        sfc.vnf_instance_ids = vnf_ids_lists

    if sfcr_ids:
        _update_sfc_flow_classifiers(sfc, sfcr_ids, update_db=False)
        sfc.sfcr_ids = sfcr_ids

    if sfcr_ids or vnf_ids_lists:
        db.update_sfc(sfc)

def _update_sfc_flow_classifiers(sfc, sfcr_ids, update_db=True):
    body = {
                "port_chain": {
                    "flow_classifiers": sfcr_ids,
                }
            }

    req = requests.put("{}{}{}".format(base_url, "/v2.0/sfc/port_chains/", sfc.id),
        json=body,
        headers={'X-Auth-Token': client.get_token()})

    if req.status_code != 200:
        log.error(req.text)
        abort(req.status_code, req.text)

    if update_db:
        sfc.sfcr_ids = sfcr_ids
        db.update_sfc(sfc)

def _update_sfc_vnf_ids(sfc, vnf_ids_lists,  update_db=True):
    old_port_pairs = _get_all_port_pairs_of_sfc(sfc.id)
    old_pp_groups = _get_existing_port_pair_groups(sfc.id)

    if (len(old_pp_groups) != len(vnf_ids_lists)):
        messages = "number of new port_pair_groups (or vnf types) " \
                    "is different from the original"
        log.error(messages)
        abort(400, messages)

    port_ids_list = []
    for vnf_ids in vnf_ids_lists:
        port_ids = [_get_data_port(vnf_id) for vnf_id in vnf_ids]
        port_ids_list.append(port_ids)

    postfix_name = "{}_{}".format(sfc.sfc_name, str(uuid.uuid4()))
    new_port_pairs_list = _create_port_pairs(postfix_name, port_ids_list, allow_existing_pp=True)
    _update_port_pair_groups(old_pp_groups, new_port_pairs_list)

    if update_db:
        sfc.vnf_instance_ids = vnf_ids_lists
        db.update_sfc(sfc)

    new_port_pairs = [pp for row in new_port_pairs_list for pp in row]

    for port_pair in old_port_pairs:
        if port_pair not in new_port_pairs:
            _delete_port_pair(port_pair)

def _get_existing_port_pair_groups(sfc_id):
    req = requests.get("{}{}{}".format(base_url, "/v2.0/sfc/port_chains/", sfc_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        log.error(req.text)
        abort(req.status_code, req.text)
    req = req.json()
    return req["port_chain"]["port_pair_groups"]

def _get_all_port_pairs_of_sfc(sfc_id):
    port_pairs = []

    req = requests.get("{}{}{}".format(base_url, "/v2.0/sfc/port_chains/", sfc_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        log.error(req.text)
        abort(req.status_code, req.text)
    req = req.json()
    pp_groups = req["port_chain"]["port_pair_groups"]

    for pp_group in pp_groups:
        req = requests.get("{}{}{}".format(base_url, "/v2.0/sfc/port_pair_groups/", pp_group),
        headers={'X-Auth-Token': client.get_token()})
        if req.status_code != 200:
            log.error(req.text)
            abort(req.status_code, req.text)
        req = req.json()
        port_pairs.extend(req["port_pair_group"]["port_pairs"])

    return port_pairs

def _update_port_pair_groups(old_pp_groups, new_port_pairs_list):
    for i, pp_group in enumerate(old_pp_groups):
        body = {
                    "port_pair_group": {
                        "port_pairs": new_port_pairs_list[i],
                    }
                }

        req = requests.put("{}{}{}".format(base_url, "/v2.0/sfc/port_pair_groups/", pp_group),
            json=body,
            headers={'X-Auth-Token': client.get_token()})

        if req.status_code != 200:
            log.error(req.text)
            abort(req.status_code, req.text)


def delete_sfc(port_chain_id):
    _delete_port_chain_recursive(port_chain_id)

def _delete_port_chain_recursive(port_chain_id):
    url = "/v2.0/sfc/port_chains"
    req = requests.get("{}{}/{}".format(base_url, url, port_chain_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        log.error(req.text)
        abort(req.status_code, req.text)
    req = req.json()
    port_pair_groups = req["port_chain"]["port_pair_groups"]
    # flow_classifiers = req["port_chain"]["flow_classifiers"]

    _delete_port_chain(port_chain_id)

    for port_pair_group in port_pair_groups:
        _delete_port_pair_group_recursive(port_pair_group)

    # for flow_classifier in flow_classifiers:
    #     delete_flow_classifier(flow_classifier)

def _delete_port_chain(port_chain_id):
    url = "/v2.0/sfc/port_chains"
    req = requests.delete("{}{}/{}".format(base_url, url, port_chain_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 204:
        log.error(req.text)
        abort(req.status_code, req.text)

def _delete_port_pair(port_pair_id):
    url = "/v2.0/sfc/port-pairs"
    req = requests.delete("{}{}/{}".format(base_url, url, port_pair_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 204:
        log.error(req.text)
        abort(req.status_code, req.text)

def _delete_port_pair_group_recursive(port_pair_group_id):
    url = "/v2.0/sfc/port_pair_groups"
    req = requests.get("{}{}/{}".format(base_url, url, port_pair_group_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        log.error(req.text)
        abort(req.status_code, req.text)
    req = req.json()
    port_pairs = req["port_pair_group"]["port_pairs"]

    _delete_port_pair_group(port_pair_group_id)

    for port_pair in port_pairs:
        _delete_port_pair(port_pair)

def _delete_port_pair_group(port_pair_group_id):
    url = "/v2.0/sfc/port_pair_groups"
    req = requests.delete("{}{}/{}".format(base_url, url, port_pair_group_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 204:
        log.error(req.text)
        abort(req.status_code, req.text)

def delete_flow_classifier(flow_classifier_id):
    url = "/v2.0/sfc/flow_classifiers"
    req = requests.delete("{}{}/{}".format(base_url, url, flow_classifier_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 204:
        log.error(req.text)
        abort(req.status_code, req.text)
