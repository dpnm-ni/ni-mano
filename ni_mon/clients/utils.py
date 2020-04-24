# -*- coding: utf-8 -*-
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client

def create_openstack_client(*args, **kwargs):
    auth = v3.Password(*args, **kwargs)
    sess = session.Session(auth=auth)
    client = keystone_client.Client(session=sess)
    return client

def get_base_urls(client):
    base_urls = dict()
    endpoints = client.endpoints.list()
    for endpoint in endpoints:
        service = client.services.get(endpoint.service_id)
        base_urls[service.type] = endpoint.url
    return base_urls
