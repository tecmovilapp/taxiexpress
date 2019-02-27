from taxiadmin.models import Passenger
from rest_framework import serializers


class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passenger
        fields = ('username', 'email', 'first_name', 'last_name')