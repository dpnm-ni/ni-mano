# coding: utf-8

"""
    NI-NFVO

    NFVO module service for the NI project.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: vantu.bkhn@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ni_nfvo_client
from ni_nfvo_client.api.vnf_api import VnfApi  # noqa: E501
from ni_nfvo_client.rest import ApiException


class TestVnfApi(unittest.TestCase):
    """VnfApi unit test stubs"""

    def setUp(self):
        self.api = ni_nfvo_client.api.vnf_api.VnfApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deploy_vnf(self):
        """Test case for deploy_vnf

        Instantiate an instance of a Vnf flavor on a given node. Return vnf ID if success  # noqa: E501
        """
        pass

    def test_destroy_vnf(self):
        """Test case for destroy_vnf

        Destroy a Vnf instance.  # noqa: E501
        """
        pass

    def test_shutdown_vnf(self):
        """Test case for shutdown_vnf

        Shut down a Vnf instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
