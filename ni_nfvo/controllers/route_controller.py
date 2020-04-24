import connexion
import datetime
import six
from threading import Timer

from ni_nfvo.models.body import Body  # noqa: E501
from ni_nfvo.models.route import Route  # noqa: E501
from ni_nfvo.models.route_update import RouteUpdate  # noqa: E501
from ni_nfvo import util

from ni_nfvo.backend_clients.sfc import create_sfc, delete_sfc, update_sfc

from ni_nfvo.database import db


def del_route(id):  # noqa: E501
    """Delete a Route.

     # noqa: E501

    :param id: route id
    :type id: str

    :rtype: None
    """

    delete_sfc(id)
    db.del_route(id)


def get_routes():  # noqa: E501
    """Get current route information, i.e., list of all active SFCRs including their paths.

     # noqa: E501


    :rtype: List[Route]
    """
    return db.get_all_routes()


def set_route(body):  # noqa: E501
    """Route a request via the provided route. Return route id if success (which also means input route id is ommitted).

     # noqa: E501

    :param body: Route information including SFCR ID and vnf instance ids.
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Route.from_dict(connexion.request.get_json())  # noqa: E501
    route_id = create_sfc(body.sfc_name, body.sfcr_ids, body.vnf_instance_ids, body.is_symmetric)
    body.id = route_id
    db.insert_route(body)

    return route_id

def update_route(id, body):  # noqa: E501
    """Update a route path.

     # noqa: E501

    :param id: route id
    :type id: str
    :param body: Route Update info.
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = RouteUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return update_sfc(id, body.sfcr_ids, body.vnf_instance_ids)
