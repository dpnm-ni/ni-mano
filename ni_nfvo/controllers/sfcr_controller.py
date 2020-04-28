import connexion
import datetime
import six
import time
import uuid

from ni_nfvo.models.sfcr import Sfcr  # noqa: E501
from ni_nfvo.models.sfcr_spec import SfcrSpec  # noqa: E501
from ni_nfvo.database import db
from ni_nfvo import util

from ni_nfvo.backend_clients import sfc as sfc_service


def add_sfcr(sfcr_spec):  # noqa: E501
    """Add new Sfc request. return sfcr ID if success

     # noqa: E501

    :param sfcr_spec: Sfc request object to be added.
    :type sfcr_spec: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        sfcr_spec = SfcrSpec.from_dict(connexion.request.get_json())  # noqa: E501
        sfcr = Sfcr.from_dict(sfcr_spec.to_dict())
        sfcr.arrivaltime = datetime.datetime.now()

        flow_classifier_id = sfc_service.create_flow_classifier(sfcr_spec)

        sfcr.id = flow_classifier_id
        db.insert_sfcr(sfcr)

        return flow_classifier_id

def del_sfcr(id):  # noqa: E501
    """Delete a sfcr.

     # noqa: E501

    :param id: route id
    :type id: str

    :rtype: None
    """
    sfc_service.delete_flow_classifier(id)
    db.del_sfcr(id)


def get_sfcrs():  # noqa: E501
    """Get currently active Sfc requests.

     # noqa: E501


    :rtype: List[Sfcr]
    """
    return db.get_all_sfcrs()
