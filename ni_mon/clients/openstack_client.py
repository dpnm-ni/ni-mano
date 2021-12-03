# -*- coding: utf-8 -*-
import requests
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client
from ni_mon.config import cfg

from flask import abort

class OpenstackClient():
    def __init__(self, auth_cfg):
        _auth = v3.Password(**auth_cfg)
        _sess = session.Session(auth=_auth)
        self.client = keystone_client.Client(session=_sess)
        self.client.authenticate(**auth_cfg)
        self.base_urls = self.get_base_urls()

    def get_base_urls(self):
        base_urls = dict()
        endpoints = self.client.endpoints.list()
        for endpoint in endpoints:
            service = self.client.services.get(endpoint.service_id)
            base_urls[service.type] = endpoint.url
        return base_urls

    def get_network_data(self, url, params=None):
        base_url = self.base_urls["network"]
        headers = {'X-Auth-Token': self.client.session.get_token()}
        req = requests.get("{}{}".format(base_url, url),
            params=params,
            headers=headers)
        if req.status_code == 200:
            return req.json()
        else:
            abort(req.status_code, req.text)


    def get_compute_data(self, url, params=None):
        base_url = self.base_urls["compute"]
        headers = {'X-Auth-Token': self.client.session.get_token()}
        req = requests.get("{}{}".format(base_url, url),
            params=params,
            headers=headers)
        if req.status_code == 200:
            return req.json()
        else:
            abort(req.status_code, req.text)

openstack_client = OpenstackClient(cfg["openstack_client"]["auth"])
