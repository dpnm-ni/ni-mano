# -*- coding: utf-8 -*-
import requests
import logging

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client

from flask import abort

from ni_nfvo.config import cfg

log = logging.getLogger(__name__)

class OpenstackClient():
    def __init__(self, auth_cfg):
        self.auth_cfg = auth_cfg
        self.client = self._create_openstack_client()
        self.base_urls = self._get_base_urls()

    def _create_openstack_client(self):
        auth = v3.Password(**self.auth_cfg)
        sess = session.Session(auth=auth)
        client = keystone_client.Client(session=sess)
        return client

    def _get_base_urls(self):
        self.client.authenticate(**self.auth_cfg)
        base_urls = dict()
        endpoints = self.client.endpoints.list()
        for endpoint in endpoints:
            service = self.client.services.get(endpoint.service_id)
            base_urls[service.type] = endpoint.url
        return base_urls

    def get_token(self):
        return self.client.session.get_token()

def get_net_id_from_name(net_name):
    base_url = openstack_client.base_urls["network"]

    req = requests.get("{}{}".format(base_url, "/v2.0/networks"),
        headers={'X-Auth-Token': openstack_client.get_token()})
    if req.status_code != 200:
        log.error(req.text)
        abort(req.status_code, req.text)

    for net in req.json()["networks"]:
        if net.get("name") == net_name:
            return net["id"]

    error_msg = "there is no network with name: " + net_name
    log.error(error_msg)
    abort(404, error_msg)


openstack_client = OpenstackClient(cfg["openstack_client"]["auth"])
