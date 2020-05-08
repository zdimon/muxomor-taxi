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

    def get_passengers(self,obj):
        out = []
        for item in Trip2Passenger.objects.filter(trip=obj):
            out.append(Trip2PassengerSerializer(item).data)
        return out

    class Meta:
        model = Trip
        fields = ['id', 'created_at', 'updated_at', 'passengers', 'driver', 'point_a', 'point_b']





class TripAddRequestSerializer(serializers.Serializer):
    driver_id = serializers.IntegerField()
    passenger_id = serializers.IntegerField()
    point_a_id = serializers.IntegerField(required=True)
    point_b_id = serializers.IntegerField(required=True)
    price = serializers.IntegerField(required=True)

class PassengerAddToTripRequestSerializer(serializers.Serializer):
    trip_id = serializers.IntegerField(required=True)
    passenger_id = serializers.IntegerField(required=True)
