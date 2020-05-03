from django.utils.translation import ugettext_lazy as _

from horizon import tables

class HypervisorLinkAction(tables.LinkAction):
    url = "horizon:admin:hypervisors:index"
    verbose_name = "Additional Node information"

class NodesTable(tables.DataTable):
    node_id = tables.WrappingColumn('id', verbose_name=_("ID"))
    name = tables.WrappingColumn('name', verbose_name=_("Name"))
    ip = tables.Column('ip', verbose_name=_("IP Address"))
    n_cores = tables.Column('n_cores', verbose_name=_("Num CPUs"))
    core_freq_mhz = tables.Column('core_freq_mhz', verbose_name=_("Core Frequency [MHz]"))
    ram_mb = tables.Column('ram_mb', verbose_name=_("Memory [MB]"))

    class Meta(object):
        name = "nodes"
        verbose_name = _("Nodes")
        table_actions = (tables.FilterAction, HypervisorLinkAction, )
