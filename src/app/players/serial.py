from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from django.db import models
# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = User
            fields = '__all__'