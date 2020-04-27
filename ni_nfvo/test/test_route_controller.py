# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ni_nfvo.models.route import Route  # noqa: E501
from ni_nfvo.models.route_spec import RouteSpec  # noqa: E501
from ni_nfvo.models.route_update_spec import RouteUpdateSpec  # noqa: E501
from ni_nfvo.test import BaseTestCase


class TestRouteController(BaseTestCase):
    """RouteController integration test stubs"""

    def test_del_route(self):
        """Test case for del_route

        Delete a Route.
        """
        response = self.client.open(
            '/routes/{id}'.format(id='id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_routes(self):
        """Test case for get_routes

        Get current route information, i.e., list of all active SFCRs including their paths.
        """
        response = self.client.open(
            '/routes',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_route(self):
        """Test case for set_route

        Route a request via the provided route. Return route ID if success.
        """
        route_spec = RouteSpec()
        response = self.client.open(
            '/routes',
            method='POST',
            data=json.dumps(route_spec),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_route(self):
        """Test case for update_route

        Update a new route path or new sfcrs.
        """
        route_update_spec = RouteUpdateSpec()
        response = self.client.open(
            '/routes/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(route_update_spec),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
