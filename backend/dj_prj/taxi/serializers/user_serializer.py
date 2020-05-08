from rest_framework import serializers
from taxi.models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = UserProfile
        fields = [  'id', 
                    'username', 
                    'publicname', 
                    'phone', 
                    'get_small_image_user_url', 
                    'get_small_image_car_url',
                    'photo_user',
                    'photo_car'
                    ]