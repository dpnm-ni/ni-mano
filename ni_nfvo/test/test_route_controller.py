# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ni_nfvo.models.route import Route  # noqa: E501
from ni_nfvo.models.route_update import RouteUpdate  # noqa: E501
from ni_nfvo.test import BaseTestCase


class TestRouteController(BaseTestCase):
    """RouteController integration test stubs"""

    def test_del_route(self):
        """Test case for del_route

        Delete a Route.
        """
        response = self.client.open(
            '/v2/routes/{id}'.format(id='id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_routes(self):
        """Test case for get_routes

        Get current route information, i.e., list of all active SFCRs including their paths.
        """
        response = self.client.open(
            '/v2/routes',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_route(self):
        """Test case for set_route

        Route a request via the provided route. Return route id if success (which also means input route id is ommitted).
        """
        body = Route()
        response = self.client.open(
            '/v2/routes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_route(self):
        """Test case for update_route

        Update a new route path or new sfcrs.
        """
        body = RouteUpdate()
        response = self.client.open(
            '/v2/routes/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
