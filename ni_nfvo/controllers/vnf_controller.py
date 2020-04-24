import connexion
import datetime
import six

from ni_nfvo.models.body import Body  # noqa: E501

from ni_nfvo.backend_clients.server import create_server, stop_server, destroy_server


def deploy_vnf(body):  # noqa: E501
    """Instantiate an instance of a VNF flavor on a given node.

     # noqa: E501

    :param body: Flavor of VNF instance to be deployed as well as the target node.
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501

    return create_server(body.vnf_name, body.flavor_id, body.node_name, body.user_data)

def shutdown_vnf(body):  # noqa: E501
    """Shut down a VNF instance.

     # noqa: E501

    :param body: ID of VNF instance to be shut down.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = VNFID.from_dict(connexion.request.get_json())  # noqa: E501
    return stop_server(body.id)

def destroy_vnf(id):  # noqa: E501
    """Destroy a VNF instance.

     # noqa: E501

    :param id: vnf id
    :type id: str

    :rtype: None
    """

    return destroy_server(id)
