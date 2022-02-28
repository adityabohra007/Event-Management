from dataclasses import field
from rest_framework import serializers

from users.models import UserProfile
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['user']