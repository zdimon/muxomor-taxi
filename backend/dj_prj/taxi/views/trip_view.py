from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.serializers import ValidationError
from taxi.models import Trip, UserProfile, Trip2Passenger, Point
from taxi.serializers import TripSerializer, TripAddRequestSerializer , PassengerAddToTripRequestSerializer

from rest_framework.serializers import ValidationError

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
        
        t = Trip()
        if "driver_id" in request.data:
            t.driver = UserProfile.objects.get(pk=request.data.get('driver_id'))
        t.point_a = Point.objects.get(pk=request.data.get('point_a_id'))
        t.point_b = Point.objects.get(pk=request.data.get('point_b_id'))
        t.price = request.data.get('price') 
        t.save()

        if "passenger_id" in request.data:
            p = UserProfile.objects.get(pk=request.data.get('driver_id'))
            t2p = Trip2Passenger()
            t2p.trip = t
            t2p.passenger = p
            t2p.save()
        return Response(TripSerializer(t).data)


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
        try:
            t = Trip.objects.get(pk=request.data.get('trip_id'))
            p = UserProfile.objects.get(pk=request.data.get('passenger_id'))
        except:
            raise ValidationError('Error! Wrong damn ids!!!')
        p2t = Trip2Passenger()
        p2t.trip = t
        p2t.passenger = p
        p2t.save()
        return Response(TripSerializer(t).data)