# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ni_nfvo.models.vnf_spec import VNFSpec  # noqa: E501
from ni_nfvo.test import BaseTestCase


class TestVnfController(BaseTestCase):
    """VnfController integration test stubs"""

    def test_deploy_vnf(self):
        """Test case for deploy_vnf

        Instantiate an instance of a VNF flavor on a given node. Return vnf ID if success
        """
        vnf_spec = VNFSpec()
        response = self.client.open(
            '/vnfs',
            method='POST',
            data=json.dumps(vnf_spec),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_destroy_vnf(self):
        """Test case for destroy_vnf

        Destroy a VNF instance.
        """
        response = self.client.open(
            '/vnfs/{id}'.format(id='id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_shutdown_vnf(self):
        """Test case for shutdown_vnf

        Shut down a VNF instance.
        """
        response = self.client.open(
            '/vnfs/{id}/shutdown'.format(id='id_example'),
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
