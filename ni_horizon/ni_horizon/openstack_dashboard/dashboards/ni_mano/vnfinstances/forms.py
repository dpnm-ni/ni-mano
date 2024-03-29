import logging
import time
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms

from ni_horizon.openstack_dashboard import api

import ni_nfvo_client
from ni_horizon.openstack_dashboard.api.ni_mano import ni_mon_api
from ni_horizon.openstack_dashboard.api.ni_mano import ni_nfvo_vnf_api
from ni_mon_client.rest import ApiException as NimonApiException


LOG = logging.getLogger(__name__)


def get_node_choices():
    nodes = ni_mon_api.get_nodes()
    node_choices = [(n.name, n.name) for n in nodes
                    if n.type == "compute" and n.status == "enabled"]
    # Add "all nodes" option to choice.
    node_choices.append(('__All__', 'All'))
    return node_choices


def _get_vnf_w_timeout(vnf_id, timeout):
    tout = timeout
    vnf_instance = None
    while tout > 0:
        try:
            vnf_instance = ni_mon_api.get_vnf_instance(vnf_id)
            return vnf_instance
        except NimonApiException:
            pass

        time.sleep(1)
        tout = tout - 1

    return vnf_instance


class DeployVnfinstance(forms.SelfHandlingForm):

    vnf_name = forms.CharField(max_length=255, label=_("VNF Instance Name"))

    vnfflavors = ni_mon_api.get_vnf_flavors()
    vnfflavor_choices = [(flavor.id, flavor.name) for flavor in vnfflavors]
    vnfflavor_id = forms.ChoiceField(choices=vnfflavor_choices,
                                     label=_("VNF Flavor"))

    node_name = forms.ChoiceField(choices=get_node_choices,
                                  initial=('__All__', 'All'),
                                  label=_("Deploy Node"))

    user_data = forms.CharField(widget=forms.Textarea,
                                label=_( "VNF cloud-config"),
                                empty_value=None,
                                required=False,
                                help_text="feed to cloud-config. Available for VM only")
    image_id = forms.CharField(max_length=255,
                               label=_("Image ID"),
                               empty_value=None,
                               required=False,
                               help_text="Specify ID of a custom OS image (if VM) " \
                                         "or dockerhub container image (if container)")



    def handle(self, request, data):
        try:
            # if node_name is None, ni_nfvo client will not enforce deployment
            # on any particular node.
            node_name = None if data['node_name'] == '__All__' else data['node_name']
            vnf_spec = ni_nfvo_client.VnfSpec(flavor_id=data['vnfflavor_id'],
                                              vnf_name=data['vnf_name'],
                                              node_name=node_name,
                                              user_data=data['user_data'],
                                              image_id=data['image_id'])
            vnf_id = ni_nfvo_vnf_api.deploy_vnf(vnf_spec)
            return _get_vnf_w_timeout(vnf_id, 10)
        except Exception as e:
            exceptions.handle(request, str(e))
