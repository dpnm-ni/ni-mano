# -*- coding: utf-8 -*-
import requests
import uuid
import base64
import logging

from ni_nfvo.config import cfg
from ni_nfvo.backend_clients.utils import openstack_client as client
from ni_nfvo.backend_clients.utils import zun_client, glance_client, nova_client
from ni_nfvo.backend_clients.utils import callWithNonNoneArgs

from flask import abort

log = logging.getLogger(__name__)

vnf_cfg = cfg["openstack_client"]["vnf"]
mgmt_net_id = client.get_net_id_from_name(vnf_cfg["mgmt_net_name"])
data_net_id = client.get_net_id_from_name(vnf_cfg["data_net_name"])
default_image_id = vnf_cfg["default_image_id"]


def create_vnf(vnf_spec):
    if (vnf_spec.image_id is None):
        vnf_spec.image_id = default_image_id

    if (glance_client.is_vm_image_id(vnf_spec.image_id)):
        return _create_vm(vnf_spec)
    else:
        return _create_container(vnf_spec)


def _create_container(vnf_spec):
    if vnf_spec.vnf_name:
        _server_name = vnf_spec.vnf_name
    else:
        _server_name = "vnf_{}".format(str(uuid.uuid4()))

    flavor = nova_client.client.flavors.get(vnf_spec.flavor_id)

    vnf = callWithNonNoneArgs(zun_client.client.containers.run,
            name=_server_name,
            cpu=flavor.vcpus,
            memory=flavor.ram,
            command=vnf_spec.command,
            image=vnf_spec.image_id,
            host=vnf_spec.node_name,
            labels={"flavor_id": vnf_spec.flavor_id},
            # default params
            image_driver="docker",
            interactive=True,
            tty=True,
            nets=[
                    {"network": mgmt_net_id},
                    {"network": data_net_id},
                ],
        )

    return vnf.uuid, 200


def _create_vm(vnf_spec):
    base_url = client.base_urls["compute"]
    headers = {'X-Auth-Token': client.get_token()}

    if vnf_spec.user_data is not None:
        user_data = base64.b64encode(vnf_spec.user_data.encode('ascii'))
    else:
        user_data = ''

    if vnf_spec.vnf_name:
        _server_name = vnf_spec.vnf_name
    else:
        _server_name = "vnf_{}".format(str(uuid.uuid4()))

    data = {
                "server": {
                    "name" : _server_name,
                    "imageRef" : vnf_spec.image_id,
                    "flavorRef" : vnf_spec.flavor_id,
                    "user_data" : user_data,
                    "networks": [
                        {"uuid": mgmt_net_id},
                        {"uuid": data_net_id},
                    ],
                }
            }

    if vnf_spec.node_name is not None:
        # FIXME: this assume the availability zone is nova. However, if
        # the host does not belong to nova zone, somehow command still works ...
        data["server"]["availability_zone"]="nova:{}".format(vnf_spec.node_name)

    url = "/servers"
    req = requests.post("{}{}".format(base_url, url),
        json=data,
        headers=headers)
    # if req is accepted (202), then return ID of server with success code (200)
    if req.status_code == 202:
        return req.json()["server"]["id"], 200
    else:
        log.error(req.text)
        abort(req.status_code, req.text)

def stop_server(vnf_id):
    if zun_client.is_container(vnf_id):
        zun_client.client.containers.stop(vnf_id)
    else:
        base_url = client.base_urls["compute"]
        url = "/servers/{}/action".format(vnf_id)
        headers = {'X-Auth-Token': client.get_token()}

        data = {
                    "os-stop" : "dummy"
                }

        req = requests.post("{}{}".format(base_url, url),
            json=data,
            headers=headers)

        if req.status_code != 202:
            log.error(req.text)
            abort(req.status_code, req.text)

def destroy_server(vnf_id):
    if zun_client.is_container(vnf_id):
        zun_client.zun_client.containers.kill(vnf_id)
    else:
        base_url = client.base_urls["compute"]
        url = "/servers/{}".format(vnf_id)
        headers = {'X-Auth-Token': client.get_token()}

        req = requests.delete("{}{}".format(base_url, url),
            headers=headers)

        if req.status_code != 204:
            log.error(req.text)
            abort(req.status_code, req.text)
