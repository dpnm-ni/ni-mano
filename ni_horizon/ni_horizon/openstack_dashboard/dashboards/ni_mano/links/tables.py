from django.utils.translation import ugettext_lazy as _

from horizon import tables


class LinksTable(tables.DataTable):
    link_id = tables.Column('id', verbose_name=_('Link ID'))
    node1_name = tables.Column('node1_id', verbose_name=_('Frist Node'))
    node2_name = tables.Column('node2_id', verbose_name=_('Second node'))
    delay_us = tables.Column('delay_us', verbose_name=_('Delay [us]'))
    max_bw_mbps = tables.Column('max_bw_mbps', verbose_name=_('Maximum throughput [Mbps]'))

    class Meta(object):
        name = "links"
        verbose_name = _("Links")
        table_actions = (tables.FilterAction,)
