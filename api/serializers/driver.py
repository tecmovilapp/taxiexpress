from taxiadmin.models import Driver
from rest_framework import serializers

from api.serializers.user import UserSerializer
from api.serializers.vehicle import VehicleSerializer


class DriverSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    rating = serializers.FloatField(label='RATING', read_only=True)
    identifier = serializers.CharField(max_length=30,  default='')
    picture =  serializers.CharField(max_length=500, default='')
    phone = serializers.CharField(max_length=500, default='')	

    user = UserSerializer()
    vehicle = VehicleSerializer()
