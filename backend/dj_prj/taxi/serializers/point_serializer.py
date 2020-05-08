from rest_framework import serializers
from taxi.models import Point

class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = ['id', 'name', 'city', 'region']