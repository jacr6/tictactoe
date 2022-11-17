from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serial import *
from .ports import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserPlatformList(APIView):
    queryset = User.objects.all() 
    serializer_class = PlatformSerializer
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = PlatformSerializer
        res = user.hello()
        res = {"res":res}
        return Response(res)