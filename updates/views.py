import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from .models import Update
from django.core.serializers import serialize
from CreatApi.mixin import JsonResponseMixin


def json_example_view(request):
    data = {
        "count" : 1000,
        "content" : "Some new Content"
    }
    json_data = json.dumps(data)
    return(HttpResponse(json_data,content_type="application/json"))

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        data = {
            "count" : 2000,
            "content" : "Some new Content"

        }
        return(JsonResponse(data))

#class JsonResponseMixin(object):
#    def render_to_json_response(self,context,**reponse_kwargs):

#       return(JsonResponse(get_data(context),**reponse_kwargs))

#    def get_data(self,context):
#        return(context)


class JsonCBV2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data = {
            "count": 2000,
            "content": "Some extra content"
        }
        return(self.render_to_json_response(data))



class SerializedDetailView(View):
    def get(self,request ,*args,**kwargs):
        obj = Update.objects.get(id=1)
#        data = {
#            "user": obj.user.username,
#            "content" : obj.content

#        }
#       json_data = json.dumps(data)
        json_data = obj.serialize()
        return(HttpResponse(json_data, content_type='application/json'))

class SerializedListView(View):
    def get(self,request,*args,**kwargs):
        qs = Update.objects.all()
#        data = serialize("json",qs, fields=('user','content'))
#        print(data)
#        json_data = data
        json_data = qs.serialize()
        return(HttpResponse(json_data, content_type="application/json"))

