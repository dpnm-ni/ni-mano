from __future__ import print_function
import nfvo_client
import time
from datetime import datetime, timedelta
from nfvo_client.rest import ApiException as NfvoApiException
from ni_mon_client.rest import ApiException as NimonApiException
from pprint import pprint
from tests.config import cfg
from tests.test_ni_mon import ni_mon_api

import pytest

nfvo_client_cfg = nfvo_client.Configuration()
nfvo_client_cfg.host = cfg["ni_nfvo"]["host"]

ni_nfvo_vnf_api = nfvo_client.VnfApi(nfvo_client.ApiClient(nfvo_client_cfg))
ni_nfvo_sfcr_api = nfvo_client.SfcrApi(nfvo_client.ApiClient(nfvo_client_cfg))
ni_nfvo_route_api = nfvo_client.RouteApi(nfvo_client.ApiClient(nfvo_client_cfg))


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

    # get nodes
    nodes = ni_mon_api.get_nodes()

    # deploy vnf
    vnf_fw_spec = nfvo_client.Body(flavor_id=flavor_id,
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
    sfcr_spec = nfvo_client.SFCR(name=sfcr_name,
                                 source_client=source_client,
                                 destination_client=destination_client,
                                 arrivaltime=datetime.now(),
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


def check_route_exist(route_id):
    routes = ni_nfvo_route_api.get_routes()
    for route in routes:
        if route.id == route_id:
            return True
    return False


def create_sample_route(sfc_name, sfcr_id, vnf_instance_id, is_symmetric):
    route_spec = nfvo_client.Route(sfc_name=sfc_name,
                                   sfcr_ids=[sfcr_id],
                                   vnf_instance_ids=[[vnf_instance_id]],
                                   is_symmetric=is_symmetric)
    route_id = ni_nfvo_route_api.set_route(route_spec)
    assert check_route_exist(route_id) == True

    return route_id


def update_sample_route(route_id, new_vnf_instance_id):
    route_update_spec = nfvo_client.RouteUpdate(vnf_instance_ids=[[new_vnf_instance_id]])
    ni_nfvo_route_api.update_route(route_id, route_update_spec)


def delete_sample_route(route_id):
    ni_nfvo_route_api.del_route(route_id)
    assert check_route_exist(route_id) == False


def test_ni_nfvo():
    vnf_fw1_id = deploy_vnf_from_flavor('vnf.fw.1.512', 'ci-fw1')
    vnf_fw2_id = deploy_vnf_from_flavor('vnf.fw.1.512', 'ci-fw2')
    client1_id = deploy_vnf_from_flavor('vnf.generic.1.512', 'ci-c1')
    client2_id = deploy_vnf_from_flavor('vnf.generic.1.512', 'ci-c2')

    sfcr_id = create_sample_sfcr('ci-sfcr', client1_id, client2_id)
    route_id = create_sample_route('ci-route', sfcr_id, vnf_fw1_id, True)
    update_sample_route(route_id, vnf_fw2_id)
    delete_sample_route(route_id)
    delete_sample_sfcr(sfcr_id)

    # should be able to recreate and delete again
    time.sleep(2)
    sfcr_id = create_sample_sfcr('ci-sfcr', client1_id, client2_id)
    route_id = create_sample_route('ci-route', sfcr_id, vnf_fw1_id, False)
    update_sample_route(route_id, vnf_fw2_id)
    delete_sample_route(route_id)
    delete_sample_sfcr(sfcr_id)

    destroy_vnf(vnf_fw1_id)
    destroy_vnf(vnf_fw2_id)
    destroy_vnf(client1_id)
    destroy_vnf(client2_id)




