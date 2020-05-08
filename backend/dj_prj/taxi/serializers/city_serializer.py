from rest_framework import serializers
from taxi.models import City, Region

from taxi.serializers import RegionSerializer

class CitySerializer(serializers.HyperlinkedModelSerializer):
    regions = serializers.SerializerMethodField()

    def get_regions(self,obj):
        out = []
        for item in Region.objects.filter(city=obj):
            out.append(RegionSerializer(item).data)
        return out

    class Meta:
        model = City
        fields = ['id', 'name', 'regions']