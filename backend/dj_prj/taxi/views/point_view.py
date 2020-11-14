from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics



from taxi.models import Point
from taxi.serializers import PointSerializer
from taxi.filters import PointFilter

class AddPointView(generics.CreateAPIView):
    '''
    Add a new point.

    _______________________

    '''
    serializer_class = PointSerializer
    permission_classes = [IsAuthenticated]

class SearchPointView(generics.ListAPIView):
    '''
    Search point.

    _______________________

    '''
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = [AllowAny]
    filterset_class = PointFilter
    
    