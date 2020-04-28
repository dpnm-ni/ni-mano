# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ni_nfvo.models.sfc import Sfc  # noqa: E501
from ni_nfvo.models.sfc_spec import SfcSpec  # noqa: E501
from ni_nfvo.models.sfc_update_spec import SfcUpdateSpec  # noqa: E501
from ni_nfvo.test import BaseTestCase


class TestSfcController(BaseTestCase):
    """SfcController integration test stubs"""

    def test_del_sfc(self):
        """Test case for del_sfc

        Delete a Sfc.
        """
        response = self.client.open(
            '/sfcs/{id}'.format(id='id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_sfcs(self):
        """Test case for get_sfcs

        Get current sfc information, i.e., list of all active Sfcrs including their paths.
        """
        response = self.client.open(
            '/sfcs',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_sfc(self):
        """Test case for set_sfc

        Create a Sfc. Return sfc ID if success.
        """
        sfc_spec = SfcSpec()
        response = self.client.open(
            '/sfcs',
            method='POST',
            data=json.dumps(sfc_spec),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_sfc(self):
        """Test case for update_sfc

        Update a new sfc path or new sfcrs.
        """
        sfc_update_spec = SfcUpdateSpec()
        response = self.client.open(
            '/sfcs/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(sfc_update_spec),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
