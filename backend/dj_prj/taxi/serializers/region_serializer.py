from rest_framework import serializers
from taxi.models import Region


class RegionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Region
        fields = ['id', 'name']