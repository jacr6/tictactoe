from rest_framework import routers
from app.users.views import *
from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)   


class Api():
    def __init__(self, *args):
        self.urls =[]
    
api = Api()

api.urls=[
    
    url(r'hello', UserPlatformList.as_view(), "")
]
api.urls = format_suffix_patterns(api.urls)