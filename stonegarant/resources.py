from django.utils import simplejson
from django.core.serializers import json
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from stonegarant.models import Memorial

class PrettyJSONSerializer(Serializer):
    json_indent = 2

    def to_json(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder,
                sort_keys=True, ensure_ascii=False, indent=self.json_indent)

class MemorialResource(ModelResource):
    class Meta:
        queryset = Memorial.objects.all()
        allowed_methods = ['get']
        resource_name = 'memorial'
        serializer = PrettyJSONSerializer()

# class MemorialResource(ModelResource):
#     class Meta:
#         queryset = Firm.objects.all()
#         resource_name = 'firm'
#         #excludes = ['isstore', 'ecwid', 'totalvotes', 'raiting', 'rating']
#         authorization = DjangoAuthorization()
#         serializer = PrettyJSONSerializer()
#         filtering = {
#             'container': ALL,
#             'parent': ALL,
#             'map_style': ALL_WITH_RELATIONS,
#         }