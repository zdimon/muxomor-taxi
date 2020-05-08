from rest_framework import serializers
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.decorators import action

from taxi.models import City
from taxi.serializers import CitySerializer
from rest_framework.generics import ListAPIView

class RegionsListView(ListAPIView):
    '''
    Список городов с регионами.
    
    _________________

    '''
    serializer_class = CitySerializer
    pagination_class = None

    def get_queryset(self):
        return City.objects.all().order_by('-id')
