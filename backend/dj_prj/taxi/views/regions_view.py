from rest_framework import serializers
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.decorators import action

from taxi.models import City
from taxi.serializers import CitySerializer
from rest_framework.generics import ListAPIView
from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

class RegionsListView(ListAPIView):
    '''
    Cities list with the regions.
    
    _________________

    '''
    serializer_class = CitySerializer
    pagination_class = None
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [TokenHasReadWriteScope]
    def get_queryset(self):
        return City.objects.all().order_by('-id')
