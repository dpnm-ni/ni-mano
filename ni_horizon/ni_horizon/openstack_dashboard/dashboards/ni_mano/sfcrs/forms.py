import logging
import json

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms

from ni_horizon.openstack_dashboard import api

import ni_nfvo_client
from ni_horizon.openstack_dashboard.api.ni_mano import ni_mon_api
from ni_horizon.openstack_dashboard.api.ni_mano import ni_nfvo_sfcr_api


LOG = logging.getLogger(__name__)


class CreateSfcr(forms.SelfHandlingForm):

    sfcr_name = forms.CharField(max_length=255, label=_('sfcr_name'))
    nf_chain = forms.CharField(max_length=1024, label=_('nf_chain'))
    nf_chain.widget.attrs['placeholder'] = '["fw", "ids"]'
    source_client = forms.CharField(max_length=255, label=_('source_client'))
    destination_client = forms.CharField(max_length=255,
                                         required=False,
                                         empty_value=None,
                                         label=_('destination_client'))
    src_ip_prefix = forms.CharField(max_length=255,
                                    required=False,
                                    empty_value=None,
                                    label=_('src_ip_prefix'))
    dst_ip_prefix = forms.CharField(max_length=255,
                                    required=False,
                                    empty_value=None,
                                    label=_('dst_ip_prefix'))
    src_port_min = forms.IntegerField(required=False,
                                      label=_('src_port_min'))
    src_port_max = forms.IntegerField(required=False,
                                      label=_('src_port_max'))
    dst_port_min = forms.IntegerField(required=False,
                                      label=_('dst_port_min'))
    dst_port_max = forms.IntegerField(required=False,
                                      label=_('dst_port_max'))
    proto = forms.CharField(max_length=255,
                            required=False,
                            empty_value=None,
                            label=_('proto'))
    bw = forms.IntegerField(required=False,
                            label=_('bw'))
    delay = forms.IntegerField(required=False,
                               label=_('delay'))
    # duration = forms.IntegerField(required=False, label=_('duration'))


    def handle(self, request, data):
        try:
            # Django use blank string, OpenAPI use None
            for k in data:
                if data[k] == "":
                    data[k] = None

            sfcr_spec = ni_nfvo_client.SfcrSpec(name=data['sfcr_name'],
                                 source_client=data['source_client'],
                                 destination_client=data['destination_client'],
                                 src_ip_prefix = data['src_ip_prefix'],
                                 dst_ip_prefix = data['dst_ip_prefix'],
                                 src_port_min=data['src_port_min'],
                                 src_port_max=data['src_port_max'],
                                 dst_port_min=data['dst_port_min'],
                                 dst_port_max=data['dst_port_max'],
                                 bw=data['bw'],
                                 delay=data['delay'],
                                 # duration=data['duration'],
                                 nf_chain=json.loads(data['nf_chain']),
                                 proto=data['proto'])
            sfcr_id = ni_nfvo_sfcr_api.add_sfcr(sfcr_spec)

            sfcrs = ni_nfvo_sfcr_api.get_sfcrs()
            for sfcr in sfcrs:
                if sfcr.id == sfcr_id:
                    return sfcr
            raise Exception()
            return sfcrs
        except Exception as e:
            exceptions.handle(request, str(e))
