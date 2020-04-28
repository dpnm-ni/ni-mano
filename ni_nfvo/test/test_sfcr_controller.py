# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ni_nfvo.models.sfcr import Sfcr  # noqa: E501
from ni_nfvo.models.sfcr_spec import SfcrSpec  # noqa: E501
from ni_nfvo.test import BaseTestCase


class TestSfcrController(BaseTestCase):
    """SfcrController integration test stubs"""

    def test_add_sfcr(self):
        """Test case for add_sfcr

        Add new Sfc request. return sfcr ID if success
        """
        sfcr_spec = SfcrSpec()
        response = self.client.open(
            '/sfcrs',
            method='POST',
            data=json.dumps(sfcr_spec),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_sfcr(self):
        """Test case for del_sfcr

        Delete a sfcr.
        """
        response = self.client.open(
            '/sfcrs/{id}'.format(id='id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_sfcrs(self):
        """Test case for get_sfcrs

        Get currently active Sfc requests.
        """
        response = self.client.open(
            '/sfcrs',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
