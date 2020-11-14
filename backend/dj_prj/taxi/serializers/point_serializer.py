from rest_framework import serializers
from taxi.models import Point
from taxi.serializers.city_serializer import CitySerializer


class PointSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Point
        fields = ['id', 'name', 'city', 'region']