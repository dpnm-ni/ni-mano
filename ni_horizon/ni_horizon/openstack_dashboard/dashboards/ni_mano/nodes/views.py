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

from django.utils.translation import ugettext_lazy as _

from horizon import tables

from ni_horizon.openstack_dashboard.api.ni_mano import ni_mon_api

from ni_horizon.openstack_dashboard.dashboards.ni_mano.nodes \
    import tables as ni_mano_nodes_tables


class IndexView(tables.DataTableView):
    table_class = ni_mano_nodes_tables.NodesTable
    page_title = _("Compute Nodes")

    def get_data(self):
        nodes = ni_mon_api.get_nodes()
        return nodes
