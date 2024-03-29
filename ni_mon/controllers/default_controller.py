# -*- coding: utf-8 -*-
import connexion
import six

from ni_mon.models.link import Link  # noqa: E501
from ni_mon.models.monitoring_entry import MonitoringEntry  # noqa: E501
from ni_mon.models.node import Node  # noqa: E501
from ni_mon.models.vnf_flavor import VNFFlavor  # noqa: E501
from ni_mon.models.vnf_instance import VNFInstance  # noqa: E501
from ni_mon.models.topology import Topology  # noqa: E501
from ni_mon.models.network_port import NetworkPort  # noqa: E501
from ni_mon import util

from ni_mon.clients import influxdb_client
from ni_mon.clients.openstack_client import openstack_client
from ni_mon.clients.zun_client import zun_client
from zunclient.v1.containers import Container
from ni_mon.config import cfg, topo

from flask import abort


def get_measurement_types(id):  # noqa: E501
    """get a list of measurements of a vnf instance or a compute node

     # noqa: E501

    :param id: The id of the vnf instance or compute node
    :type id: str

    :rtype: List[str]
    """
    return influxdb_client.get_measurement_types(id)


def get_last_measurement(id, measurement_type):  # noqa: E501
    """Return the latest value of a measurement of a vnf instance or compute node

     # noqa: E501

    :param id: The id of the vnf instance or compute node
    :type id: str
    :param measurement_type: The measurement metric, which can be get using getMeasurementTypes()
    :type measurement_type: str

    :rtype: MonitoringEntry
    """
    return influxdb_client.get_last_measurement(id, measurement_type)

def get_measurement(id, measurement_type, start_time, end_time):  # noqa: E501
    """Return the value of a measurement of a vnf instance or compute node at a timestamp or a timestamp period

     # noqa: E501

    :param id: The id of the vnf instance or compute node
    :type id: str
    :param measurement_type: The measurement metric, which can be get using getMeasurementTypes()
    :type measurement_type: str
    :param start_time: starting time to get the measurement
    :type start_time: str
    :param end_time: ending time to get the measurement
    :type end_time: str

    :rtype: List[MonitoringEntry]
    """

    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)

    # Remove time zone info (which is GMT) as it can cause timezone problem
    start_time = start_time.replace(tzinfo=None)
    end_time = end_time.replace(tzinfo=None)

    return influxdb_client.get_measurements(id,
            measurement_type,
            float(start_time.timestamp()),
            float(end_time.timestamp())
        )


def get_link(id):  # noqa: E501
    """get a link

     # noqa: E501

    :param id: The id of the link
    :type id: str

    :rtype: Link
    """
    raw_links = topo.get("links")
    if raw_links is None:
        abort(404)

    for link in raw_links:
        if str(link["id"]) == id:
            return Link(
                id=link["id"],
                node1_id=link["node1_id"],
                node2_id=link["node2_id"],
                delay_us=link["delay_us"],
                max_bw_mbps=link["max_bw_mbps"]
            )

    abort(404)


def get_link_between_nodes(node1_id, node2_id):  # noqa: E501
    """get detailed information of a link between two specific nodes

     # noqa: E501

    :param node1_id: The id of the first node in the link
    :type node1_id: str
    :param node2_id: The id of the second node in the link
    :type node2_id: str

    :rtype: Link
    """
    raw_links = topo.get("links")
    if raw_links is None:
        abort(404)

    for link in raw_links:
        if ((str(link["node1_id"]) == node1_id and str(link["node2_id"]) == node2_id) or
                (str(link["node1_id"]) == node2_id and str(link["node2_id"]) == node1_id)
            ):
            return Link(
                id=link["id"],
                node1_id=node1_id,
                node2_id=node2_id,
                delay_us=link["delay_us"],
                max_bw_mbps=link["max_bw_mbps"]
            )

    abort(404)


def get_links():  # noqa: E501
    """get list of link

     # noqa: E501


    :rtype: List[Link]
    """
    raw_links = topo.get("links")
    if raw_links is None:
        return None

    links = []
    for link in raw_links:
        links.append(
            Link(
                    id=link["id"],
                    node1_id=link["node1_id"],
                    node2_id=link["node2_id"],
                    delay_us=link["delay_us"],
                    max_bw_mbps=link["max_bw_mbps"]
                )
            )
    return links


def get_node(id):  # noqa: E501
    """get information of a node

     # noqa: E501

    :param id: The id of the node
    :type id: str

    :rtype: Node
    """

    nodes = get_nodes()
    for node in nodes:
        if node.id == id:
            return node
    abort(404)


def get_nodes():  # noqa: E501
    """get a list of nodes

     # noqa: E501


    :rtype: List[Node]
    """
    raw_nodes = openstack_client.get_compute_data("/os-hypervisors/detail")
    # node_names = [raw_node["hypervisor_hostname"] for raw_node in raw_nodes.get("hypervisors")]
    raw_nodes = raw_nodes.get("hypervisors")
    if raw_nodes is None:
        abort(404)
    nodes = []
    # for node_name in node_names:
    #     nodes.append(get_node(node_name))
    for topo_node in topo.get("nodes"):
        ip = None
        n_cores = None
        ram_mb = None
        n_cores_free = None
        ram_free_mb = None
        status = None
        core_freq_mhz = topo_node.get("core_freq_MHz")
        ram_freq_mhz = topo_node.get("ram_freq_MHz")

        if topo_node["type"] == "compute":
            for raw_node in raw_nodes:
                if topo_node["id"] == raw_node["hypervisor_hostname"]:
                    ip=raw_node["host_ip"]
                    n_cores=raw_node["vcpus"]
                    ram_mb=raw_node["memory_mb"]
                    status=raw_node["status"]
                    n_cores_free=raw_node["vcpus"] - raw_node["vcpus_used"]
                    ram_free_mb=raw_node["free_ram_mb"]
                    break

        node = Node(
                # in some case, we need to use compute node name,
                # thus we use node name (hostname) as the node id
                id=topo_node["id"],
                name=topo_node["id"],
                type=topo_node["type"],
                ip=ip,
                n_cores=n_cores,
                core_freq_mhz=core_freq_mhz,
                ram_mb=ram_mb,
                ram_freq_mhz=ram_freq_mhz,
                status=status,
                n_cores_free=n_cores_free,
                ram_free_mb=ram_free_mb,
            )

        nodes.append(node)

    return nodes


def get_topology():  # noqa: E501
    """Return a topology with lists of node names and link ids

     # noqa: E501


    :rtype: Topology
    """

    topology = Topology()
    topology.nodes = [node["id"] for node in topo.get("nodes")]
    topology.links = [link["id"] for link in topo.get("links")]

    return topology


def get_vnf_flavor(id):  # noqa: E501
    """get detailed information of a vnfflavor

     # noqa: E501

    :param id: The id of the vnfflavor
    :type id: str

    :rtype: VNFFlavor
    """
    raw_flavor = openstack_client.get_compute_data(
            "/flavors/{flavors_id}".format(flavors_id=id)
        )
    raw_flavor = raw_flavor.get("flavor")
    if raw_flavor is None:
        abort(404)

    # extra specs API link:
    # https://github.com/openstack/nova/blob/master/api-ref/source/os-flavor-extra-specs.inc
    extra_specs = openstack_client.get_compute_data(
            "/flavors/{flavors_id}/os-extra_specs".format(flavors_id=id)
        )
    extra_specs = extra_specs.get("extra_specs")
    os_image_id = extra_specs.get("os_image_id")
    capacity_mbps = extra_specs.get("capacity_mbps")
    delay_us = extra_specs.get("delay_us")

    if capacity_mbps is None or delay_us is None:
        abort(404, "Missing properties: capacity_mbps: %s, delay_us: %s in flavor %s" %(capacity_mbps, delay_us, raw_flavor["name"]))
    if os_image_id is None:
        abort(404, "Missing internal property: os_image_id: %s in flavor %s" %(os_image_id, raw_flavor["name"]))

    vnfflavor = VNFFlavor(
            id=raw_flavor["id"],
            name=raw_flavor["name"],
            capacity_mbps=capacity_mbps,
            delay_us=delay_us,
            n_cores=raw_flavor["vcpus"],
            ram_mb=raw_flavor["ram"],
        )

    return vnfflavor


def get_vnf_flavors():  # noqa: E501
    """get a list of vnfflavors

     # noqa: E501


    :rtype: List[VNFFlavor]
    """
    raw_flavors = openstack_client.get_compute_data("/flavors")
    raw_flavors = raw_flavors.get("flavors")
    if raw_flavors is None:
        abort(404)

    vnfflavors = []
    # vnf flavor name starts with 'vnf'
    for raw_flavor in raw_flavors:
        if raw_flavor["name"].split('.')[0] == 'vnf':
            vnfflavors.append(get_vnf_flavor(raw_flavor["id"]))

    return vnfflavors


def get_vnf_instance(id):  # noqa: E501
    """get detailed information of a vnf instance

     # noqa: E501

    :param id: The id of the vnf instance
    :type id: str

    :rtype: VNFInstance
    """

    raw_vnf = openstack_client.get_compute_data(
            "/servers/{server_id}".format(server_id=id)
        )
    raw_vnf = raw_vnf.get("server")
    if raw_vnf is None:
        abort(404)

    network_ports = openstack_client.get_network_data(
            "v2.0/ports?device_id={server_id}".format(server_id=id)
        )
    raw_ports = network_ports.get("ports")
    if raw_ports is not None:
        ports = [ _get_ports(raw_port) for raw_port in raw_ports ]

    vnf_instance = _get_vnf_instance(raw_vnf, ports)

    return vnf_instance


def get_vnf_instances():  # noqa: E501
    """get a list of vnf instances

     # noqa: E501


    :rtype: List[VNFInstance]
    """

    vnfs = []
    raw_vms = openstack_client.get_compute_data("/servers/detail")
    raw_vms = raw_vms.get("servers")
    if raw_vms is not None:
        vnfs.extend(raw_vms)

    containers = zun_client.client.containers.list()
    if len(containers) > 0:
        vnfs.extend(containers)

    raw_ports = openstack_client.get_network_data("v2.0/ports")
    raw_ports = raw_ports.get("ports")
    if raw_ports is None:
        abort(404)

    vnf_infos = []
    for vnf in vnfs:
        ports = []
        for raw_port in raw_ports:
            vnf_id = vnf.uuid if type(vnf) == Container else vnf["id"]
            if raw_port["device_id"] == vnf_id:
                port = _get_ports(raw_port)
                ports.append(port)

        vnf_info = _get_vnf_instance(vnf, ports)
        vnf_infos.append(vnf_info)
    return vnf_infos


def _get_ports(raw_port):
    return NetworkPort(
            raw_port["id"],
            _get_port_name(raw_port["id"]),
            raw_port["network_id"],
            [ip["ip_address"] for ip in raw_port["fixed_ips"]]
        )


def _get_vnf_instance(vnf, ports):
    if type(vnf) == Container:
        return VNFInstance(
            id=vnf.uuid,
            name=vnf.name,
            status=vnf.status,
            # node id is the same as host
            node_id=vnf.host,
            flavor_id=vnf.labels.get("flavor_id"),
            ports=ports,
            image_id=vnf.image,
            is_container=True
        )
    else:
        return VNFInstance(
            id=vnf["id"],
            name=vnf["name"],
            status=vnf["status"],
            flavor_id=vnf["flavor"]["id"],
            # node id is the same as hostname
            node_id=vnf["OS-EXT-SRV-ATTR:host"],
            ports=ports,
            image_id=vnf["image"]["id"],
            is_container=False
        )


def _get_port_name(port_id):
    # this is how openstack map the port id to port name
    return "tap%s" %(port_id[:11])
