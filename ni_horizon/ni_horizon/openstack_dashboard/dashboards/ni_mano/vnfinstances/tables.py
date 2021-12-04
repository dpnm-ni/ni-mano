from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy
from django.utils.translation import pgettext_lazy
from django import urls

from horizon import tables

from ni_horizon.openstack_dashboard.api.ni_mano import ni_nfvo_vnf_api
from ni_horizon.openstack_dashboard.api.ni_mano import ni_mon_api



class DeployVnfinstanceAction(tables.LinkAction):
    name = "vnfinstance"
    verbose_name = _("Deploy VNF instance")
    url = "horizon:ni_mano:vnfinstances:deploy_vnfinstance"
    classes = ("ajax-modal",)
    icon = "cloud-upload"

    def allowed(self, request, instance=None):
        return True


class DeleteVnfinstanceAction(tables.DeleteAction):
    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Destroy",
            u"Destroy",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Scheduled deletion of VNF Instance",
            u"Scheduled deletion of VNF Instances",
            count
        )

    def delete(self, request, obj_id):
        ni_nfvo_vnf_api.destroy_vnf(obj_id)

    def allowed(self, request, instance=None):
        return instance is not None


class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, instance_id):
        vnfinstance = ni_mon_api.get_vnf_instance(instance_id)
        return vnfinstance


def get_ips(vnfinstance):
    ips = []
    for port in vnfinstance.ports:
        # this is how openstack map port_id to ovs tap name
        net_if_name = "tap" + port.port_id[:11]
        ips.append('%s: %s' % (net_if_name, port.ip_addresses))
    return ", ".join(ips)


def get_vnf_type(vnfinstance):
    if vnfinstance.is_container == True:
        return "Container"
    else:
        return "VM"


def get_vnf_detail_link(vnfinstance):
    if vnfinstance.is_container == True:
        # its in angular, so cannot do urls.reverse. So I do it the hardway here...
        return "/dashboard/ngdetails/OS::Zun::Container/{}".format(vnfinstance.id)
    else:
        return urls.reverse("horizon:admin:instances:detail", args=(vnfinstance.id,))


class VnfinstancesTable(tables.DataTable):

    STATUS_CHOICES = (
        ("active", True),
        ("shutoff", True),
        ("suspended", True),
        ("paused", True),
        ("error", False),
        ("rescue", True),
        ("shelved", True),
        ("shelved_offloaded", True),
        # for container
        ("running", True),
    )

    STATUS_DISPLAY_CHOICES = (
        ("deleted", pgettext_lazy("Current status of an Instance", u"Deleted")),
        ("active", pgettext_lazy("Current status of an Instance", u"Active")),
        ("shutoff", pgettext_lazy("Current status of an Instance", u"Shutoff")),
        ("suspended", pgettext_lazy("Current status of an Instance",
                                    u"Suspended")),
        ("paused", pgettext_lazy("Current status of an Instance", u"Paused")),
        ("error", pgettext_lazy("Current status of an Instance", u"Error")),
        ("resize", pgettext_lazy("Current status of an Instance",
                                 u"Resize/Migrate")),
        ("verify_resize", pgettext_lazy("Current status of an Instance",
                                        u"Confirm or Revert Resize/Migrate")),
        ("revert_resize", pgettext_lazy(
            "Current status of an Instance", u"Revert Resize/Migrate")),
        ("reboot", pgettext_lazy("Current status of an Instance", u"Reboot")),
        ("hard_reboot", pgettext_lazy("Current status of an Instance",
                                      u"Hard Reboot")),
        ("password", pgettext_lazy("Current status of an Instance", u"Password")),
        ("rebuild", pgettext_lazy("Current status of an Instance", u"Rebuild")),
        ("migrating", pgettext_lazy("Current status of an Instance",
                                    u"Migrating")),
        ("build", pgettext_lazy("Current status of an Instance", u"Build")),
        ("rescue", pgettext_lazy("Current status of an Instance", u"Rescue")),
        ("soft-delete", pgettext_lazy("Current status of an Instance",
                                      u"Soft Deleted")),
        ("shelved", pgettext_lazy("Current status of an Instance", u"Shelved")),
        ("shelved_offloaded", pgettext_lazy("Current status of an Instance",
                                            u"Shelved Offloaded")),
        # these vm states are used when generating CSV usage summary
        ("building", pgettext_lazy("Current status of an Instance", u"Building")),
        ("stopped", pgettext_lazy("Current status of an Instance", u"Stopped")),
        ("rescued", pgettext_lazy("Current status of an Instance", u"Rescued")),
        ("resized", pgettext_lazy("Current status of an Instance", u"Resized")),
        # for container
        ("running", pgettext_lazy("Current status of an Instance", u"Running")),
    )


    instance_id = tables.Column('id', verbose_name=_('ID'))
    name = tables.Column('name', link=get_vnf_detail_link, verbose_name=_('Name'))
    ips = tables.Column(get_ips, verbose_name=_('IP Addresses'))
    vnf_type = tables.Column(get_vnf_type, verbose_name=_('VNF Type'))
    status = tables.Column('status',
        status=True,
        status_choices=STATUS_CHOICES,
        display_choices=STATUS_DISPLAY_CHOICES,
        verbose_name=_('Status')
    )
    flavor_id = tables.Column('flavor_id', verbose_name=_('Flavor ID'))
    node_id = tables.Column('node_id', verbose_name=_('Node ID'))

    class Meta(object):
        name = "vnfinstances"
        verbose_name = _("Vnfinstances")
        status_columns = ["status",]
        row_class = UpdateRow
        table_actions = (tables.FilterAction, DeployVnfinstanceAction,)
        row_actions = (DeleteVnfinstanceAction,)
