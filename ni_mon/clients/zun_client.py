# -*- coding: utf-8 -*-
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client
import zunclient.client
from ni_nfvo.config import cfg


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

zun_client = ZunClient(cfg["openstack_client"]["auth"])
