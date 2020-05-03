# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from horizon import tables
from horizon import forms

from django.utils.translation import ugettext_lazy as _

from django.urls import reverse
from django.urls import reverse_lazy

from ni_horizon.openstack_dashboard.dashboards.ni_mano.vnfinstances \
    import tables as ni_mano_vnfinstances_tables

from ni_horizon.openstack_dashboard.dashboards.ni_mano.vnfinstances \
    import forms as ni_mano_vnfinstances_forms

from ni_horizon.openstack_dashboard.api.ni_mano import ni_mon_api


class IndexView(tables.DataTableView):
    table_class = ni_mano_vnfinstances_tables.VnfinstancesTable
    page_title = _("VNF Instances")

    def get_data(self):
        vnfinstances = ni_mon_api.get_vnf_instances()
        return vnfinstances

class DeployVnfinstanceView(forms.ModalFormView):
    form_class = ni_mano_vnfinstances_forms.DeployVnfinstance
    template_name = 'ni_mano/vnfinstances/deploy_vnfinstance.html'
    modal_id = "deploy_vnfinstance_modal"
    modal_header = _("Deploy VNF Instance")
    submit_label = _("Deploy VNF Instance")
    submit_url = reverse_lazy("horizon:ni_mano:vnfinstances:deploy_vnfinstance")
    success_url = reverse_lazy("horizon:ni_mano:vnfinstances:index")

