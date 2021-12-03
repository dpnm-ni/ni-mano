# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ni_mon.models.link import Link  # noqa: E501
from ni_mon.models.monitoring_entry import MonitoringEntry  # noqa: E501
from ni_mon.models.node import Node  # noqa: E501
from ni_mon.models.topology import Topology  # noqa: E501
from ni_mon.models.vnf_flavor import VNFFlavor  # noqa: E501
from ni_mon.models.vnf_instance import VNFInstance  # noqa: E501
from ni_mon.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_last_measurement(self):
        """Test case for get_last_measurement

        Return the latest value of a measurement of a vnf instance or compute node
        """
        response = self.client.open(
            '/last_measurement/{id}/{measurement_type}'.format(id='id_example', measurement_type='measurement_type_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_link(self):
        """Test case for get_link

        get a link
        """
        response = self.client.open(
            '/link/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_link_between_nodes(self):
        """Test case for get_link_between_nodes

        get detailed information of a link between two specific nodes
        """
        query_string = [('node1_id', 'node1_id_example'),
                        ('node2_id', 'node2_id_example')]
        response = self.client.open(
            '/link_between_nodes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_links(self):
        """Test case for get_links

        get list of link
        """
        response = self.client.open(
            '/links',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_measurement(self):
        """Test case for get_measurement

        Return the value of a measurement of a vnf instance or compute node at a timestamp or a timestamp period
        """
        query_string = [('start_time', '2013-10-20T19:20:30+01:00'),
                        ('end_time', '2013-10-20T19:20:30+01:00')]
        response = self.client.open(
            '/measurements/{id}/{measurement_type}'.format(id='id_example', measurement_type='measurement_type_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_measurement_types(self):
        """Test case for get_measurement_types

        get a list of measurements of a vnf instance or a compute node
        """
        response = self.client.open(
            '/measurement_types/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_node(self):
        """Test case for get_node

        get information of a node
        """
        response = self.client.open(
            '/nodes/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_nodes(self):
        """Test case for get_nodes

        get a list of nodes
        """
        response = self.client.open(
            '/nodes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_topology(self):
        """Test case for get_topology

        Return a topology with lists of node names and link ids
        """
        response = self.client.open(
            '/topology',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vnf_flavor(self):
        """Test case for get_vnf_flavor

        get detailed information of a vnfflavor. Only available to VM (container do not have flavor)
        """
        response = self.client.open(
            '/vnfflavors/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vnf_flavors(self):
        """Test case for get_vnf_flavors

        get a list of vnfflavors
        """
        response = self.client.open(
            '/vnfflavors',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vnf_instance(self):
        """Test case for get_vnf_instance

        get detailed information of a vnf instance
        """
        response = self.client.open(
            '/vnfinstances/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vnf_instances(self):
        """Test case for get_vnf_instances

        get a list of vnf instances
        """
        response = self.client.open(
            '/vnfinstances',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
