from django.conf.urls import url
from django.urls import path, re_path
from .views import (
    UpdateModelAPI,
    UpdateListView

)

urlpatterns = [
    re_path(r'',UpdateListView.as_view()),
#    re_path(r'^(?P<id>[0-9]{1})/$', UpdateModelAPI.as_view())
    re_path(r'^(?P<id>\d+/)?$',UpdateModelAPI.as_view()),
#    path('json/serialized/list', UpdateListView.as_view()),

]