from django.utils.translation import ugettext_lazy as _

from horizon import tables

class FlavorLinkAction(tables.LinkAction):
    url = "horizon:admin:flavors:index"
    verbose_name = "Additional VNF flavor information"

class VnfflavorsTable(tables.DataTable):
    vnfflavor_id = tables.Column('id', verbose_name=_('ID'))
    name = tables.Column('name', verbose_name=_('Name'))
    capacity_mbps = tables.Column('capacity_mbps', verbose_name=_('Capacity [Mbps]'))
    delay_us = tables.Column('delay_us', verbose_name=_('Delay [us]'))
    n_cores = tables.Column('n_cores', verbose_name=_('Number of CPU cores'))
    ram_mb = tables.Column('ram_mb', verbose_name=_('Memory [MB]'))

    class Meta(object):
        name = "vnfflavors"
        verbose_name = _("Vnfflavors")
        table_actions = (tables.FilterAction, FlavorLinkAction, )
