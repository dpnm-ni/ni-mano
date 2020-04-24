from __future__ import print_function
import ni_mon_client
from datetime import datetime, timedelta
from tests.config import cfg
from ni_mon_client.rest import ApiException
from pprint import pprint

import pytest

ni_mon_client_cfg = ni_mon_client.Configuration()
ni_mon_client_cfg.host = cfg["ni_mon"]["host"]

ni_mon_api = ni_mon_client.DefaultApi(ni_mon_client.ApiClient(ni_mon_client_cfg))


def test_link():
    links = ni_mon_api.get_links()
    assert len(links) > 0

    for i in range(0, len(links)):
        assert links[i] == ni_mon_api.get_link(links[i].id)
        assert links[i] == ni_mon_api.get_link_between_nodes(links[i].node1_id, links[i].node2_id)


def test_node():
    nodes = ni_mon_api.get_nodes()
    assert len(nodes) > 0

    for i in range(0, len(nodes)):
        assert nodes[i] == ni_mon_api.get_node(nodes[i].id)


def test_vnf_flavor():
    vnf_flavors = ni_mon_api.get_vnf_flavors()
    assert len(vnf_flavors) > 0
    for i in range(0, len(vnf_flavors)):
        assert vnf_flavors[i] == ni_mon_api.get_vnf_flavor(vnf_flavors[i].id)


def test_vnf_instances():
    vnf_instances = ni_mon_api.get_vnf_instances()
    assert len(vnf_instances) > 0
    for i in range(0, len(vnf_instances)):
        assert vnf_instances[0] == ni_mon_api.get_vnf_instance(vnf_instances[0].id)


def test_get_topology():
    topo = ni_mon_api.get_topology()
    assert len(topo.nodes) > 0
    assert len(topo.links) > 0


def test_measurement_vnf():
    vnf_sample_id = None
    vnf_instances = ni_mon_api.get_vnf_instances()
    for vnf_instance in vnf_instances:
        if vnf_instance.name == 'vnf_sample_do_not_delete':
            vnf_sample_id = vnf_instance.id
            break

    assert vnf_sample_id != None

    measurement_types = ni_mon_api.get_measurement_types(vnf_sample_id)
    assert len(measurement_types) > 0

    for measurement_type in measurement_types:
        current_dt = datetime.now()
        past_dt = current_dt - timedelta(seconds=30)
        measurement_results = ni_mon_api.get_measurement(vnf_sample_id, measurement_type, past_dt, current_dt)
        assert len(measurement_results) > 0


def test_measurement_node():
    nodes = ni_mon_api.get_nodes()
    for node in nodes:
        measurement_types = ni_mon_api.get_measurement_types(node.name)

        for measurement_type in measurement_types:
            current_dt = datetime.now()
            past_dt = current_dt - timedelta(seconds=30)
            measurement_results = ni_mon_api.get_measurement(node.name, measurement_type, past_dt, current_dt)
            assert len(measurement_results) > 0
