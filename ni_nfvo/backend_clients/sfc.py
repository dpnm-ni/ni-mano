# -*- coding: utf-8 -*-
import requests
import uuid

from ni_nfvo.config import cfg
from ni_nfvo.backend_clients.utils import get_net_id_from_name
from ni_nfvo.backend_clients.utils import openstack_client as client
from ni_nfvo.database import db

from flask import abort
from flask import current_app

vnf_cfg = cfg["openstack_client"]["vnf"]
data_net_id = get_net_id_from_name(vnf_cfg["data_net_name"])
base_url = client.base_urls["network"]


def create_sfc(fc_prefix, sfcr_ids, vnf_ids_lists, is_symmetric=False):
    if len(vnf_ids_lists) == 0:
        error_message = "vnf list is empty"
        current_app.logger.error(error_message)
        abort(404, error_message)

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
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)

    req = req.json()

    for port in req["ports"]:
        if port["network_id"] == data_net_id:
            return port["id"]

    error_message = "no data port for vnf id: {}".format(vnf_instance_id)
    current_app.logger.error(error_message)
    abort(400, error_message)

def create_flow_classifier(sfcr):
    url = "/v2.0/sfc/flow_classifiers"

    body = dict()
    # logical_source_port is required
    body["logical_source_port"] = _get_data_port(sfcr.source_client)

    if sfcr.destination_client is not None:
        body["logical_destination_port"] = _get_data_port(sfcr.destination_client)

    if sfcr.src_ip_prefix is not None:
        body["source_ip_prefix"] = sfcr.src_ip_prefix
    if sfcr.dst_ip_prefix is not None:
        body["destination_ip_prefix"] = sfcr.dst_ip_prefix
    if sfcr.src_port_min is not None:
        body["source_port_range_min"] = sfcr.src_port_min
    if sfcr.src_port_max is not None:
        body["source_port_range_max"] = sfcr.src_port_max
    if sfcr.dst_port_min is not None:
        body["destination_port_range_min"] = sfcr.dst_port_min
    if sfcr.dst_port_max is not None:
        body["destination_port_range_max"] = sfcr.dst_port_max
    if sfcr.proto is not None:
        body["protocol"] = sfcr.proto

    body = {"flow_classifier": body}

    req = requests.post("{}{}".format(base_url, url),
        json=body,
        headers={'X-Auth-Token': client.get_token()})

    if req.status_code == 201:
        return req.json()["flow_classifier"]["id"]
    else:
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)


def _create_port_pairs(postfix_name, port_ids_list, allow_existing_pp=False):
    # create port_pairs from ports. Use the same port for ingress and egress

    req = requests.get("{}{}".format(base_url, "/v2.0/sfc/port_pairs"),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        current_app.logger.error(req.text)
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
                    current_app.logger.error(req.text)
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
            current_app.logger.error(req.text)
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
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)


def update_sfc(route_id, sfcr_ids=None, vnf_ids_lists=None):
    route = db.get_route(route_id)
    if route is None:
        error_message = "route_id: {} not found".format(route_id)
        current_app.logger.error(error_message)
        abort(404, error_message)

    if vnf_ids_lists:
        _update_sfc_vnf_ids(route, vnf_ids_lists, update_db=False)
        route.vnf_instance_ids = vnf_ids_lists

    if sfcr_ids:
        _update_sfc_flow_classifiers(route, sfcr_ids, update_db=False)
        route.sfcr_ids = sfcr_ids

    if sfcr_ids or vnf_ids_lists:
        db.update_route(route)

def _update_sfc_flow_classifiers(route, sfcr_ids, update_db=True):
    body = {
                "port_chain": {
                    "flow_classifiers": sfcr_ids,
                }
            }

    req = requests.put("{}{}{}".format(base_url, "/v2.0/sfc/port_chains/", route.id),
        json=body,
        headers={'X-Auth-Token': client.get_token()})

    if req.status_code != 200:
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)

    if update_db:
        route.sfcr_ids = sfcr_ids
        db.update_route(route)

def _update_sfc_vnf_ids(route, vnf_ids_lists,  update_db=True):
    old_port_pairs = _get_all_port_pairs_of_route(route.id)
    old_pp_groups = _get_existing_port_pair_groups(route.id)

    if (len(old_pp_groups) != len(vnf_ids_lists)):
        messages = "number of new port_pair_groups (or vnf types) " \
                    "is different from the original"
        current_app.logger.error(messages)
        abort(400, messages)

    port_ids_list = []
    for vnf_ids in vnf_ids_lists:
        port_ids = [_get_data_port(vnf_id) for vnf_id in vnf_ids]
        port_ids_list.append(port_ids)

    postfix_name = "{}_{}".format(route.sfc_name, str(uuid.uuid4()))
    new_port_pairs_list = _create_port_pairs(postfix_name, port_ids_list, allow_existing_pp=True)
    _update_port_pair_groups(old_pp_groups, new_port_pairs_list)

    if update_db:
        route.vnf_instance_ids = vnf_ids_lists
        db.update_route(route)

    new_port_pairs = [pp for row in new_port_pairs_list for pp in row]

    for port_pair in old_port_pairs:
        if port_pair not in new_port_pairs:
            _delete_port_pair(port_pair)

def _get_existing_port_pair_groups(route_id):
    req = requests.get("{}{}{}".format(base_url, "/v2.0/sfc/port_chains/", route_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)
    req = req.json()
    return req["port_chain"]["port_pair_groups"]

def _get_all_port_pairs_of_route(route_id):
    port_pairs = []

    req = requests.get("{}{}{}".format(base_url, "/v2.0/sfc/port_chains/", route_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)
    req = req.json()
    pp_groups = req["port_chain"]["port_pair_groups"]

    for pp_group in pp_groups:
        req = requests.get("{}{}{}".format(base_url, "/v2.0/sfc/port_pair_groups/", pp_group),
        headers={'X-Auth-Token': client.get_token()})
        if req.status_code != 200:
            current_app.logger.error(req.text)
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
            current_app.logger.error(req.text)
            abort(req.status_code, req.text)


def delete_sfc(port_chain_id):
    _delete_port_chain_recursive(port_chain_id)

def _delete_port_chain_recursive(port_chain_id):
    url = "/v2.0/sfc/port_chains"
    req = requests.get("{}{}/{}".format(base_url, url, port_chain_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        current_app.logger.error(req.text)
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
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)

def _delete_port_pair(port_pair_id):
    url = "/v2.0/sfc/port-pairs"
    req = requests.delete("{}{}/{}".format(base_url, url, port_pair_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 204:
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)

def _delete_port_pair_group_recursive(port_pair_group_id):
    url = "/v2.0/sfc/port_pair_groups"
    req = requests.get("{}{}/{}".format(base_url, url, port_pair_group_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 200:
        current_app.logger.error(req.text)
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
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)

def delete_flow_classifier(flow_classifier_id):
    url = "/v2.0/sfc/flow_classifiers"
    req = requests.delete("{}{}/{}".format(base_url, url, flow_classifier_id),
        headers={'X-Auth-Token': client.get_token()})
    if req.status_code != 204:
        current_app.logger.error(req.text)
        abort(req.status_code, req.text)
