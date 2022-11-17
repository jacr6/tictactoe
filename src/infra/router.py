from rest_framework import routers
from app.players.views import *
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
router = routers.DefaultRouter()
router.register(r'players', UserViewSet)


class Api():
    def __init__(self, *args):
        self.urls = []


api = Api()

api.urls = [

    path(r'hello', PlayerList.as_view()),
    path(r'join', PlayerList.as_view()),
    path(r'play', PlayerList.as_view()),
    path(r'quit', PlayerList.as_view()),
    path(r'list', PlayerList.as_view()),
]
api.urls = format_suffix_patterns(api.urls)
