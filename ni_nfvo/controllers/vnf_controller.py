import connexion
import datetime
import six

from ni_nfvo.models.vnf_spec import VNFSpec  # noqa: E501

from ni_nfvo.backend_clients.server import create_server, stop_server, destroy_server


def deploy_vnf(vnf_spec):  # noqa: E501
    """Instantiate an instance of a VNF flavor on a given node. Return vnf ID if success

     # noqa: E501

    :param vnf_spec: Flavor of VNF instance to be deployed as well as the target node.
    :type vnf_spec: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        vnf_spec = VNFSpec.from_dict(connexion.request.get_json())  # noqa: E501

    return create_server(vnf_spec.vnf_name, vnf_spec.flavor_id, vnf_spec.node_name, vnf_spec.user_data)


def shutdown_vnf(id):  # noqa: E501
    """Shut down a VNF instance.

     # noqa: E501

    :param id: ID of VNF instance to be shut down.
    :type id: str

    :rtype: None
    """
    return stop_server(id)


def destroy_vnf(id):  # noqa: E501
    """Destroy a VNF instance.

     # noqa: E501

    :param id: vnf id
    :type id: str

    :rtype: None
    """

    return destroy_server(id)
