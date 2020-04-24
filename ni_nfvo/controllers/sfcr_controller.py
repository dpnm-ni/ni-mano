import connexion
import datetime
import six
import time
import uuid

from ni_nfvo.models.sfcr import SFCR  # noqa: E501
from ni_nfvo.database import db
from ni_nfvo import util

from ni_nfvo.backend_clients.sfc import create_flow_classifier, delete_flow_classifier


def add_sfcr(body):  # noqa: E501
    """Add new SFC request.

     # noqa: E501

    :param body: SFC request object to be added.
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = SFCR.from_dict(connexion.request.get_json())  # noqa: E501
        flow_classifier_id = create_flow_classifier(body)
        body.id = flow_classifier_id
        db.insert_sfcr(body)

        return flow_classifier_id

def del_sfcr(id):  # noqa: E501
    """Delete a sfcr.

     # noqa: E501

    :param id: route id
    :type id: str

    :rtype: None
    """
    delete_flow_classifier(id)
    db.del_sfcr(id)


def get_sfcrs():  # noqa: E501
    """Get currently active SFC requests.

     # noqa: E501


    :rtype: List[SFCR]
    """
    return db.get_all_sfcrs()
