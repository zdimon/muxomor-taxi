from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.serializers import ValidationError

from taxi.serializers import TripSerializer, TripAddRequestSerializer , PassengerAddToTripRequestSerializer

class TripAddView(APIView):
    """
       Add a new trip.

       _____________________
    """
    @swagger_auto_schema( 
        request_body = TripAddRequestSerializer, \
        responses={200: TripSerializer}
        )

    def post(self, request, format=None):

        return Response({'message': 'Ok'})


class PassengerAddToTripView(APIView):
    """
       Add a new passenger to the trip.

       _____________________

    """
    @swagger_auto_schema( 
        request_body = PassengerAddToTripRequestSerializer, \
        responses={200: TripSerializer}
        )

    def post(self, request, format=None):

        return Response({'message': 'Ok'})