from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables

from ni_horizon.openstack_dashboard.api.ni_mano import ni_nfvo_sfcr_api


class CreateSfcrAction(tables.LinkAction):
    name = "sfcr"
    verbose_name = _("Create SFC Request")
    url = "horizon:ni_mano:sfcrs:create_sfcr"
    classes = ("ajax-modal",)
    icon = "cloud-upload"

    def allowed(self, request, instance=None):
        return True

class DeleteSfcrAction(tables.DeleteAction):
    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Delete ",
            u"Delete s",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Scheduled deletion of ",
            u"Scheduled deletion of s",
            count
        )

    def delete(self, request, obj_id):
        ni_nfvo_sfcr_api.del_sfcr(obj_id)

    def allowed(self, request, instance=None):
        return instance is not None


def get_flow_classifier(sfcr):
    return "%s:(%s-%s)\n-> %s:(%s-%s), %s" % (sfcr.src_ip_prefix,
                                                 sfcr.src_port_min,
                                                 sfcr.src_port_max,
                                                 sfcr.dst_ip_prefix,
                                                 sfcr.dst_port_min,
                                                 sfcr.dst_port_max,
                                                 sfcr.proto)


def get_sfc_endpoint(sfcr):
    return "%s\n-> %s" % (sfcr.source_client, sfcr.destination_client)


class SfcrsTable(tables.DataTable):


    sfcr_id = tables.Column('id', verbose_name=_('Sfcr ID'))
    name = tables.Column('name', verbose_name=_('Name'))
    arrivaltime = tables.Column('arrivaltime', verbose_name=_('Arrival Time'))
    flow_classifier = tables.Column(get_flow_classifier, verbose_name=_('Flow Classifier'))
    client_pair = tables.Column(get_sfc_endpoint, verbose_name=_('Sfc Endpoints'))
    bw = tables.Column('bw', verbose_name=_('Banwidth [Mbps]'))
    delay = tables.Column('delay', verbose_name=_('Delay [us]'))
    # duration = tables.Column('duration', verbose_name=_('duration'))
    nf_chain = tables.Column('nf_chain', verbose_name=_('Network Funtion Chain'))

    class Meta(object):
        name = "sfcrs"
        verbose_name = _("Sfcrs")
        table_actions = (tables.FilterAction, CreateSfcrAction,)
        row_actions = (DeleteSfcrAction,)
