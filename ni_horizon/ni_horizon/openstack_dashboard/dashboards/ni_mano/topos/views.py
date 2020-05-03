import json
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader

from horizon.utils.lazy_encoder import LazyTranslationEncoder

from ni_horizon.openstack_dashboard.api.ni_mano import ni_mon_api

class IndexView(View):

    def _get_links(self):
        return [item.to_dict() for item in ni_mon_api.get_links()]


    def _get_routers(self):
        return [item.to_dict() for item in ni_mon_api.get_nodes() if item.type == "switch"]


    def _get_computes(self):
        return [item.to_dict() for item in ni_mon_api.get_nodes() if item.type == "compute"]


    def _get_vnf_instances(self):
        return [item.to_dict() for item in ni_mon_api.get_vnf_instances()]


    def get(self, request, *args, **kwargs):
        template = loader.get_template('ni_mano/topos/index.html')
        data = {'routers': self._get_routers(),
                'computes': self._get_computes(),
                'links': self._get_links(),
                'vnfs': self._get_vnf_instances()
                }
        json_string = json.dumps(data, cls=LazyTranslationEncoder,
                                 ensure_ascii=False)
        # return HttpResponse(json_string, content_type='text/json')
        return HttpResponse(template.render({"topo_data": json_string}, request))

