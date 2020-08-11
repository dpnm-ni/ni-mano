# -*- coding: utf-8 -*-
import requests
import uuid
import base64
import logging

from ni_nfvo.config import cfg
from ni_nfvo.backend_clients.utils import get_net_id_from_name
from ni_nfvo.backend_clients.utils import openstack_client as client

from flask import abort

log = logging.getLogger(__name__)

vnf_cfg = cfg["openstack_client"]["vnf"]
mgmt_net_id = get_net_id_from_name(vnf_cfg["mgmt_net_name"])
data_net_id = get_net_id_from_name(vnf_cfg["data_net_name"])

def create_server(server_name, flavor_id, host_name, custom_user_data, image_id):
    # extra specs API link: https://github.com/openstack/nova/blob/master/api-ref/source/os-flavor-extra-specs.inc
    base_url = client.base_urls["compute"]
    headers = {'X-Auth-Token': client.get_token()}

    url = "/flavors/{flavors_id}/os-extra_specs".format(flavors_id=flavor_id)
    req = requests.get("{}{}".format(base_url, url),
        headers=headers)
    if req.status_code != 200:
        log.error(req.text)
        abort(req.status_code, req.text)

    extra_specs = req.json()
    try:
        os_image_id = image_id if image_id is not None else extra_specs["extra_specs"]["os_image_id"]
        default_user_data = extra_specs["extra_specs"].get("default_user_data")
    except Exception as e:
        return str(e), 404

    if custom_user_data is not None:
        user_data = base64.b64encode(custom_user_data.encode('ascii'))
    elif default_user_data is not None:
        # store user_data in extra_specs convert \n to \\n. need to restore
        default_user_data = default_user_data.replace('\\n', '\n')
        user_data = base64.b64encode(default_user_data.encode('ascii'))
    else:
        user_data = ''

    if server_name:
        _server_name = server_name
    else:
        _server_name = "vnf_{}".format(str(uuid.uuid4()))

    data = {
                "server": {
                    "name" : _server_name,
                    "imageRef" : os_image_id,
                    "flavorRef" : flavor_id,
                    "user_data" : user_data,
                    "networks": [
                        {"uuid": mgmt_net_id},
                        {"uuid": data_net_id},
                    ],
                }
            }

    if host_name is not None:
        # FIXME: this assume the availability zone is nova. However, if
        # the host does not belong to nova zone, somehow command still works ...
        data["server"]["availability_zone"]="nova:{}".format(host_name)

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

def stop_server(server_id):
    base_url = client.base_urls["compute"]
    url = "/servers/{}/action".format(server_id)
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

def destroy_server(server_id):
    base_url = client.base_urls["compute"]
    url = "/servers/{}".format(server_id)
    headers = {'X-Auth-Token': client.get_token()}

    req = requests.delete("{}{}".format(base_url, url),
        headers=headers)

    if req.status_code != 204:
        log.error(req.text)
        abort(req.status_code, req.text)
