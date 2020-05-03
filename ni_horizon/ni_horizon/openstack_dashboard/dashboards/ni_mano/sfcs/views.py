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
from horizon import tabs
from horizon import forms

from django.utils.translation import ugettext_lazy as _

from django.urls import reverse
from django.urls import reverse_lazy

from ni_horizon.openstack_dashboard.dashboards.ni_mano.sfcs \
    import tables as ni_mano_sfcs_tables

from ni_horizon.openstack_dashboard.dashboards.ni_mano.sfcs \
    import forms as ni_mano_sfcs_forms

from ni_horizon.openstack_dashboard.api.ni_mano import ni_nfvo_sfc_api

class IndexView(tables.DataTableView):
    table_class = ni_mano_sfcs_tables.SfcsTable
    page_title = _("SFCs")

    def get_data(self):
        sfcs = ni_nfvo_sfc_api.get_sfcs()
        return sfcs

class CreateSfcView(forms.ModalFormView):
    form_class = ni_mano_sfcs_forms.CreateSfc
    template_name = 'ni_mano/sfcs/create_sfc.html'
    modal_id = "create_sfc_modal"
    modal_header = _("Create SFC")
    submit_label = _("Create SFC")
    submit_url = reverse_lazy("horizon:ni_mano:sfcs:create_sfc")
    success_url = reverse_lazy("horizon:ni_mano:sfcs:index")

