import connexion
import datetime
import six
from threading import Timer

from ni_nfvo.models.sfc import Sfc  # noqa: E501
from ni_nfvo.models.sfc_spec import SfcSpec  # noqa: E501
from ni_nfvo.models.sfc_update_spec import SfcUpdateSpec  # noqa: E501
from ni_nfvo import util

from ni_nfvo.backend_clients import sfc as sfc_service

from ni_nfvo.database import db


def del_sfc(id):  # noqa: E501
    """Delete a Sfc.

     # noqa: E501

    :param id: sfc id
    :type id: str

    :rtype: None
    """

    sfc_service.delete_sfc(id)
    db.del_sfc(id)


def get_sfcs():  # noqa: E501
    """Get current sfc information, i.e., list of all active Sfcrs including their paths.

     # noqa: E501


    :rtype: List[Sfc]
    """
    return db.get_all_sfcs()


def set_sfc(sfc_spec):  # noqa: E501
    """Sfc a request via the provided sfc. Return sfc ID if success.

     # noqa: E501

    :param sfc_spec: Sfc information including Sfcr ID and vnf instance ids.
    :type sfc_spec: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        sfc_spec = SfcSpec.from_dict(connexion.request.get_json())  # noqa: E501

    sfc_id = sfc_service.create_sfc(sfc_spec.sfc_name,
                          sfc_spec.sfcr_ids,
                          sfc_spec.vnf_instance_ids,
                          sfc_spec.is_symmetric)

    sfc = Sfc.from_dict(sfc_spec.to_dict())
    sfc.id = sfc_id
    db.insert_sfc(sfc)

    return sfc_id


def update_sfc(id, sfc_update_spec):  # noqa: E501
    """Update a new sfc path or new sfcrs.

     # noqa: E501

    :param id: sfc id
    :type id: str
    :param sfc_update_spec: Sfc Update info.
    :type sfc_update_spec: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        sfc_update_spec = SfcUpdateSpec.from_dict(connexion.request.get_json())  # noqa: E501
    return sfc_service.update_sfc(id, sfc_update_spec.sfcr_ids, sfc_update_spec.vnf_instance_ids)
