# coding: utf-8

"""
    NI-Mon

    Monitoring module for NI project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: vantu.bkhn@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ni_mon_client
from ni_mon_client.api.default_api import DefaultApi  # noqa: E501
from ni_mon_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = ni_mon_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_link(self):
        """Test case for get_link

        get a link  # noqa: E501
        """
        pass

    def test_get_link_between_nodes(self):
        """Test case for get_link_between_nodes

        get detailed information of a link between two specific nodes  # noqa: E501
        """
        pass

    def test_get_links(self):
        """Test case for get_links

        get list of link  # noqa: E501
        """
        pass

    def test_get_measurement(self):
        """Test case for get_measurement

        Return the value of a measurement of a vnf instance or compute node at a timestamp or a timestamp period  # noqa: E501
        """
        pass

    def test_get_measurement_types(self):
        """Test case for get_measurement_types

        get a list of measurements of a vnf instance or a compute node  # noqa: E501
        """
        pass

    def test_get_node(self):
        """Test case for get_node

        get information of a node  # noqa: E501
        """
        pass

    def test_get_nodes(self):
        """Test case for get_nodes

        get a list of nodes  # noqa: E501
        """
        pass

    def test_get_topology(self):
        """Test case for get_topology

        Return a topology with lists of node names and link ids  # noqa: E501
        """
        pass

    def test_get_vnf_flavor(self):
        """Test case for get_vnf_flavor

        get detailed information of a vnfflavor  # noqa: E501
        """
        pass

    def test_get_vnf_flavors(self):
        """Test case for get_vnf_flavors

        get a list of vnfflavors  # noqa: E501
        """
        pass

    def test_get_vnf_instance(self):
        """Test case for get_vnf_instance

        get detailed information of a vnf instance  # noqa: E501
        """
        pass

    def test_get_vnf_instances(self):
        """Test case for get_vnf_instances

        get a list of vnf instances  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
