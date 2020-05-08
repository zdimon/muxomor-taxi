from rest_framework import serializers
from taxi.models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'publicname', 'phone']