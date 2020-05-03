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

from ni_horizon.openstack_dashboard.dashboards.ni_mano.sfcrs \
    import tables as ni_mano_sfcrs_tables

from ni_horizon.openstack_dashboard.dashboards.ni_mano.sfcrs \
    import forms as ni_mano_sfcrs_forms

from ni_horizon.openstack_dashboard.api.ni_mano import ni_nfvo_sfcr_api

class IndexView(tables.DataTableView):
    table_class = ni_mano_sfcrs_tables.SfcrsTable
    page_title = _("SFC Requests")

    def get_data(self):
        # Add data to the context here...
        # return context
        sfcrs = ni_nfvo_sfcr_api.get_sfcrs()
        return sfcrs

class CreateSfcrView(forms.ModalFormView):
    form_class = ni_mano_sfcrs_forms.CreateSfcr
    template_name = 'ni_mano/sfcrs/create_sfcr.html'
    modal_id = "create_sfcr_modal"
    modal_header = _("Create SFC Request")
    submit_label = _("Create SFC Request")
    submit_url = reverse_lazy("horizon:ni_mano:sfcrs:create_sfcr")
    success_url = reverse_lazy("horizon:ni_mano:sfcrs:index")

