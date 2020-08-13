import logging
import json

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms

from ni_horizon.openstack_dashboard import api

import datetime
import ni_nfvo_client
from ni_horizon.openstack_dashboard.api.ni_mano import ni_mon_api
from ni_horizon.openstack_dashboard.api.ni_mano import ni_nfvo_sfc_api


LOG = logging.getLogger(__name__)


class CreateSfc(forms.SelfHandlingForm):

    sfc_name = forms.CharField(max_length=255, label=_('SFC Name'))
    is_symmetric = forms.BooleanField(required=False, empty_value=None, label=_('Symmetric'))
    sfcr_ids = forms.CharField(
            widget=forms.Textarea(attrs={"placeholder": '[\n"sfcr_id_1",\n"sfcr_id_2"\n]'}),
            max_length=1024,
            label=_(' IDs')
        )
    vnf_instance_ids = forms.CharField(
            widget=forms.Textarea(attrs={"placeholder": '[\n["vnf_id_1", "vnf_id_2"],\n["vnf_id_3", "vnf_id_4"]\n]'}),
            max_length=1024,
            label=_('VNF IDs')
        )


    def handle(self, request, data):
        try:
            sfc_spec = ni_nfvo_client.SfcSpec(sfc_name=data['sfc_name'],
                                   sfcr_ids=json.loads(data['sfcr_ids']),
                                   vnf_instance_ids=json.loads(data['vnf_instance_ids']),
                                   is_symmetric=data['is_symmetric'])
            sfc_id = ni_nfvo_sfc_api.set_sfc(sfc_spec)

            sfcs = ni_nfvo_sfc_api.get_sfcs()
            for sfc in sfcs:
                if sfc.id == sfc_id:
                    return sfc
            raise Exception()
        except Exception as e:
            exceptions.handle(request, str(e))
