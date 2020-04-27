import connexion
import datetime
import six
from threading import Timer

from ni_nfvo.models.route import Route  # noqa: E501
from ni_nfvo.models.route_spec import RouteSpec  # noqa: E501
from ni_nfvo.models.route_update_spec import RouteUpdateSpec  # noqa: E501
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


def set_route(route_spec):  # noqa: E501
    """Route a request via the provided route. Return route ID if success.

     # noqa: E501

    :param route_spec: Route information including SFCR ID and vnf instance ids.
    :type route_spec: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        route_spec = RouteSpec.from_dict(connexion.request.get_json())  # noqa: E501

    route_id = create_sfc(route_spec.sfc_name,
                          route_spec.sfcr_ids,
                          route_spec.vnf_instance_ids,
                          route_spec.is_symmetric)

    route = Route.from_dict(route_spec.to_dict())
    route.id = route_id
    db.insert_route(route)

    return route_id


def update_route(id, route_update_spec):  # noqa: E501
    """Update a new route path or new sfcrs.

     # noqa: E501

    :param id: route id
    :type id: str
    :param route_update_spec: Route Update info.
    :type route_update_spec: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        route_update_spec = RouteUpdateSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return update_sfc(id, route_update_spec.sfcr_ids, route_update_spec.vnf_instance_ids)
