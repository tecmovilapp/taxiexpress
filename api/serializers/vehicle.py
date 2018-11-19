from taxiadmin.models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'