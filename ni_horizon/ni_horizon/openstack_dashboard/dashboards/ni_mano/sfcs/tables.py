from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables

from ni_horizon.openstack_dashboard.api.ni_mano import ni_nfvo_sfc_api
from ni_horizon.openstack_dashboard.api.ni_mano import ni_nfvo_sfcr_api
from ni_horizon.openstack_dashboard.api.ni_mano import ni_mon_api



class CreateSfcAction(tables.LinkAction):
    name = "sfc"
    verbose_name = _("Create SFC")
    url = "horizon:ni_mano:sfcs:create_sfc"
    classes = ("ajax-modal",)
    icon = "cloud-upload"

    def allowed(self, request, instance=None):
        return True

class DeleteSfcAction(tables.DeleteAction):
    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Delete SFC",
            u"Delete SFCs",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Scheduled deletion of SFC",
            u"Scheduled deletion of SFCs",
            count
        )

    def delete(self, request, obj_id):
        ni_nfvo_sfc_api.del_sfc(obj_id)

    def allowed(self, request, instance=None):
        return instance is not None


def get_sfcr_names(sfc):
    all_sfcrs = ni_nfvo_sfcr_api.get_sfcrs()
    sfcr_names = []
    for sfcr_id in sfc.sfcr_ids:
        for sfcr in all_sfcrs:
            if sfcr_id == sfcr.id:
                sfcr_names.append(sfcr.name)
                break
    return sfcr_names


def get_vnf_names(sfc):
    all_vnf_instances = ni_mon_api.get_vnf_instances()
    vnf_names_lists = []
    for vnf_ids in sfc.vnf_instance_ids:
        vnf_names = []
        for vnf_id in vnf_ids:
            for vnf in all_vnf_instances:
                if vnf_id == vnf.id:
                    vnf_names.append(vnf.name)
                    break
        vnf_names_lists.append(vnf_names)

    return vnf_names_lists


class SfcsTable(tables.DataTable):
    sfc_id = tables.Column('id', verbose_name=_('SFC ID'))
    sfc_name = tables.Column('sfc_name', verbose_name=_('SFC Name'))
    sfcr_names = tables.Column(get_sfcr_names, verbose_name=_(' Names'))
    vnf_instance_names = tables.Column(
        get_vnf_names, verbose_name=_('VNF Names'))
    is_symmetric = tables.Column('is_symmetric', verbose_name=_('Symmetric'))

    class Meta(object):
        name = "sfcs"
        verbose_name = _("Sfcs")
        table_actions = (tables.FilterAction, CreateSfcAction,)
        row_actions = (DeleteSfcAction,)
