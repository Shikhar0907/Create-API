from django.urls import path,include
from django.urls import re_path
from django.contrib import admin
from .views import StatusAPIView, StatusAPIDetailView#,ListSearchAPIView, DetailAPIView


urlpatterns = [
#    path('',ListSearchAPIView.as_view()),
    path('',StatusAPIView.as_view()),
#    path('/Json/create/',CreateAPIView.as_view()),
    re_path(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),
#    re_path(r'^Update/(?P<pk>\d+)/$',UpdateAPIView.as_view()),
#    re_path(r'^delete/(?P<pk>\d+)/$',DeleteAPIView.as_view()),
]