import connexion
import datetime
import six

from ni_nfvo.models.vnf_spec import VnfSpec  # noqa: E501

from ni_nfvo.backend_clients import server as server_service

def deploy_vnf(vnf_spec):  # noqa: E501
    """Instantiate an instance of a Vnf flavor on a given node. Return vnf ID if success

     # noqa: E501

    :param vnf_spec: Flavor of Vnf instance to be deployed as well as the target node.
    :type vnf_spec: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        vnf_spec = VnfSpec.from_dict(connexion.request.get_json())  # noqa: E501

    return server_service.create_vnf(vnf_spec)


def shutdown_vnf(id):  # noqa: E501
    """Shut down a Vnf instance.

     # noqa: E501

    :param id: ID of Vnf instance to be shut down.
    :type id: str

    :rtype: None
    """
    return server_service.stop_server(id)


def destroy_vnf(id):  # noqa: E501
    """Destroy a Vnf instance.

     # noqa: E501

    :param id: vnf id
    :type id: str

    :rtype: None
    """

    return server_service.destroy_server(id)
