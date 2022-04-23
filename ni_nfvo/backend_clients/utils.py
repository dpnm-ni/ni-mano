# -*- coding: utf-8 -*-
import requests
import logging

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client

from flask import abort
import zunclient.client
import glanceclient.client
import novaclient.client

from ni_nfvo.config import cfg

log = logging.getLogger(__name__)

class OpenstackClient():
    def __init__(self, auth_cfg):
        self.auth_cfg = auth_cfg

        auth = v3.Password(**self.auth_cfg)
        sess = session.Session(auth=auth)
        self.client = keystone_client.Client(session=sess)

        self.base_urls = self._get_base_urls()

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


    def get_net_id_from_name(self, net_name):
        base_url = self.base_urls["network"]

        req = requests.get("{}{}".format(base_url, "/v2.0/networks"),
            headers={'X-Auth-Token': self.get_token()})
        if req.status_code != 200:
            log.error(req.text)
            abort(req.status_code, req.text)

        for net in req.json()["networks"]:
            if net.get("name") == net_name:
                return net["id"]

        error_msg = "there is no network with name: " + net_name
        log.error(error_msg)
        abort(404, error_msg)


class ZunClient():
    def __init__(self, auth_cfg):
        auth = v3.Password(**auth_cfg)
        sess = session.Session(auth=auth)
        self.client = zunclient.client.Client(session=sess)

    def is_container(self, con_id):
        try:
            self.client.containers.get(con_id)
            return True
        except zunclient.common.apiclient.exceptions.NotFound:
            return False


class GlanceClient():
    def __init__(self, auth_cfg):
        VERSION='2'
        auth = v3.Password(**auth_cfg)
        sess = session.Session(auth=auth)
        self.client = glanceclient.client.Client(VERSION, session=sess)

    def is_vm_image_id(self, image_id):
        try:
            self.client.images.get(image_id)
            return True
        except glanceclient.exc.HTTPNotFound:
            return False

    def get_id_from_name(self, image_name):
        images = self.client.images.list()
        for image in images:
            if image.name == image_name:
                return image.id
        return None



class NovaClient():
    def __init__(self, auth_cfg):
        VERSION='2'
        auth = v3.Password(**auth_cfg)
        sess = session.Session(auth=auth)
        self.client = novaclient.client.Client(VERSION, session=sess)


def callWithNonNoneArgs(f, *args, **kwargs):
    kwargsNotNone = {k: v for k, v in kwargs.items() if v is not None}
    return f(*args, **kwargsNotNone)


openstack_client = OpenstackClient(cfg["openstack_client"]["auth"])
zun_client = ZunClient(cfg["openstack_client"]["auth"])
glance_client = GlanceClient(cfg["openstack_client"]["auth"])
nova_client = NovaClient(cfg["openstack_client"]["auth"])
