"""CreatApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from updates.views import json_example_view,JsonCBV,JsonCBV2,SerializedDetailView,SerializedListView
urlpatterns = [
    path('api/auth/jwt',obtain_jwt_token),
    path('api/auth/jwt/refresh',refresh_jwt_token),
    path('api/updates',include('updates.api.urls')),
    path('api/rest/',include('RestFrameWork.api.urls')),
#    path('JsonListView/',SerializedListView.as_view()),
#    path('JsonData/',SerializedDetailView.as_view()),
#    path('JsonCBV2/',JsonCBV2.as_view()),
#    path('JsonCBV/',JsonCBV.as_view()),
#    path('', json_example_view),
    path('admin/', admin.site.urls),
]
