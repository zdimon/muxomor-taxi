from rest_framework import serializers
from taxi.models import Trip, Trip2Passenger
from taxi.serializers import UserSerializer, PointSerializer


class Trip2PassengerSerializer(serializers.ModelSerializer):
    passenger = UserSerializer()
    class Meta:
        model = Trip2Passenger
        fields = ['id', 'passenger', 'created_at']


class TripSerializer(serializers.ModelSerializer):
    passengers = serializers.SerializerMethodField()
    point_a = PointSerializer()
    point_b = PointSerializer()
    driver = UserSerializer()
    def get_passengers(self,obj):
        out = []
        for item in Trip2Passenger.objects.filter(trip=obj):
            out.append(Trip2PassengerSerializer(item).data)
        return out

    class Meta:
        model = Trip
        fields = ['id', 'created_at', 'updated_at', 'passengers', 'driver', 'point_a', 'point_b', 'price']





class TripAddRequestSerializer(serializers.Serializer):
    driver_id = serializers.IntegerField()
    passenger_id = serializers.IntegerField()
    point_a_id = serializers.IntegerField(required=True, min_value=1)
    point_b_id = serializers.IntegerField(required=True, min_value=1)
    price = serializers.IntegerField(required=True, min_value=1)

class PassengerAddToTripRequestSerializer(serializers.Serializer):
    trip_id = serializers.IntegerField(required=True, min_value=1)
    passenger_id = serializers.IntegerField(required=True, min_value=1)

class DriverAddToTripRequestSerializer(serializers.Serializer):
    trip_id = serializers.IntegerField(required=True, min_value=1)
    driver_id = serializers.IntegerField(required=True, min_value=1)