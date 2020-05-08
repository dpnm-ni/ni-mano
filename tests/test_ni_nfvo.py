from __future__ import print_function
import ni_nfvo_client
import time
from datetime import datetime, timedelta
from ni_nfvo_client.rest import ApiException as NfvoApiException
from ni_mon_client.rest import ApiException as NimonApiException
from pprint import pprint
from tests.config import cfg
from tests.test_ni_mon import ni_mon_api

import pytest

ni_nfvo_client_cfg = ni_nfvo_client.Configuration()
ni_nfvo_client_cfg.host = cfg["ni_nfvo"]["host"]

ni_nfvo_vnf_api = ni_nfvo_client.VnfApi(ni_nfvo_client.ApiClient(ni_nfvo_client_cfg))
ni_nfvo_sfcr_api = ni_nfvo_client.SfcrApi(ni_nfvo_client.ApiClient(ni_nfvo_client_cfg))
ni_nfvo_sfc_api = ni_nfvo_client.SfcApi(ni_nfvo_client.ApiClient(ni_nfvo_client_cfg))


def check_vnf_running_w_timeout(vnf_id, timeout):
    tout = timeout
    while tout > 0:
        # get vnf_instance, allow not found because vnf may not ready yet
        try:
            vnf_instance = ni_mon_api.get_vnf_instance(vnf_id)
            if vnf_instance.status == 'ACTIVE':
                break
        except NimonApiException as e:
            assert e.status == 404

        time.sleep(1)
        tout = tout - 1

    vnf_instance = ni_mon_api.get_vnf_instance(vnf_id)
    if vnf_instance.status == 'ACTIVE':
        return True
    return False


def deploy_vnf_from_flavor(flavor_name, vnf_name):
    # get flavor id
    vnf_flavors = ni_mon_api.get_vnf_flavors()
    flavor_id = None
    for vnf_flavor in vnf_flavors:
        if vnf_flavor.name == flavor_name:
            flavor_id = vnf_flavor.id
            break
    assert flavor_id != None

    # deploy vnf
    vnf_fw_spec = ni_nfvo_client.VnfSpec(flavor_id=flavor_id,
                                vnf_name=vnf_name)
    vnf_id = ni_nfvo_vnf_api.deploy_vnf(vnf_fw_spec)

    assert check_vnf_running_w_timeout(vnf_id, timeout=60) == True

    return vnf_id


def check_vnf_destroyed_w_timeout(vnf_id, timeout):
    tout = timeout
    while tout > 0:
        # get vnf_instance, if not found then vnf is destroyed
        try:
            vnf_instance = ni_mon_api.get_vnf_instance(vnf_id)
        except NimonApiException as e:
            if e.status == 404:
                return True

        time.sleep(1)
        tout = tout - 1

    return False


def destroy_vnf(vnf_id):
    ni_nfvo_vnf_api.destroy_vnf(vnf_id)
    assert check_vnf_destroyed_w_timeout(vnf_id, timeout=60) == True


def check_sfcr_exist(sfcr_id):
    sfcrs = ni_nfvo_sfcr_api.get_sfcrs()
    for sfcr in sfcrs:
        if sfcr.id == sfcr_id:
            return True
    return False


def create_sample_sfcr(sfcr_name, source_client, destination_client=None):
    sfcr_spec = ni_nfvo_client.SfcrSpec(name=sfcr_name,
                                 source_client=source_client,
                                 destination_client=destination_client,
                                 src_ip_prefix="192.0.0.8/32",
                                 src_port_min=0,
                                 src_port_max=65535,
                                 dst_port_min=0,
                                 dst_port_max=65535,
                                 proto='TCP')
    sfcr_id = ni_nfvo_sfcr_api.add_sfcr(sfcr_spec)
    assert check_sfcr_exist(sfcr_id) == True

    return sfcr_id


def delete_sample_sfcr(sfcr_id):
    ni_nfvo_sfcr_api.del_sfcr(sfcr_id)
    assert check_sfcr_exist(sfcr_id) == False


def check_sfc_exist(sfc_id):
    sfcs = ni_nfvo_sfc_api.get_sfcs()
    for sfc in sfcs:
        if sfc.id == sfc_id:
            return True
    return False


def create_sample_sfc(sfc_name, sfcr_id, vnf_instance_id, is_symmetric):
    sfc_spec = ni_nfvo_client.SfcSpec(sfc_name=sfc_name,
                                   sfcr_ids=[sfcr_id],
                                   vnf_instance_ids=[[vnf_instance_id]],
                                   is_symmetric=is_symmetric)
    sfc_id = ni_nfvo_sfc_api.set_sfc(sfc_spec)
    assert check_sfc_exist(sfc_id) == True

    return sfc_id


def update_sample_sfc(sfc_id, new_vnf_instance_id):
    sfc_update_spec = ni_nfvo_client.SfcUpdateSpec(vnf_instance_ids=[[new_vnf_instance_id]])
    ni_nfvo_sfc_api.update_sfc(sfc_id, sfc_update_spec)


def delete_sample_sfc(sfc_id):
    ni_nfvo_sfc_api.del_sfc(sfc_id)
    assert check_sfc_exist(sfc_id) == False


def test_ni_nfvo():
    vnf_fw1_id = deploy_vnf_from_flavor('vnf.fw.1.512', 'ci-fw1')
    vnf_fw2_id = deploy_vnf_from_flavor('vnf.fw.1.512', 'ci-fw2')
    client1_id = deploy_vnf_from_flavor('vnf.generic.1.512', 'ci-c1')
    client2_id = deploy_vnf_from_flavor('vnf.generic.1.512', 'ci-c2')

    sfcr_id = create_sample_sfcr('ci-sfcr', client1_id, client2_id)
    sfc_id = create_sample_sfc('ci-sfc', sfcr_id, vnf_fw1_id, True)
    update_sample_sfc(sfc_id, vnf_fw2_id)
    delete_sample_sfc(sfc_id)
    delete_sample_sfcr(sfcr_id)

    # should be able to recreate and delete again
    time.sleep(2)
    sfcr_id = create_sample_sfcr('ci-sfcr', client1_id, client2_id)
    sfc_id = create_sample_sfc('ci-sfc', sfcr_id, vnf_fw1_id, False)
    update_sample_sfc(sfc_id, vnf_fw2_id)
    delete_sample_sfc(sfc_id)
    delete_sample_sfcr(sfcr_id)

    destroy_vnf(vnf_fw1_id)
    destroy_vnf(vnf_fw2_id)
    destroy_vnf(client1_id)
    destroy_vnf(client2_id)




