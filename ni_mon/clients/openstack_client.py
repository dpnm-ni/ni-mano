# -*- coding: utf-8 -*-
import requests
from .utils import create_openstack_client, get_base_urls
from ni_mon.config import cfg

from flask import abort

auth_cfg = cfg["openstack_client"]["auth"]
_client = create_openstack_client(**auth_cfg)
_client.authenticate(**auth_cfg)
_base_urls = get_base_urls(_client)


def get_network_data(url, params=None):
    base_url = _base_urls["network"]
    headers = {'X-Auth-Token': _client.session.get_token()}
    req = requests.get("{}{}".format(base_url, url),
        params=params,
        headers=headers)
    if req.status_code == 200:
        return req.json()
    else:
        abort(req.status_code, req.text)


def get_compute_data(url, params=None):
    base_url = _base_urls["compute"]
    headers = {'X-Auth-Token': _client.session.get_token()}
    req = requests.get("{}{}".format(base_url, url),
        params=params,
        headers=headers)
    if req.status_code == 200:
        return req.json()
    else:
        abort(req.status_code, req.text)


