from taxiadmin.models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    model = serializers.CharField(read_only=True)
    made = serializers.CharField(read_only=True)
    class Meta:
        model = Vehicle
        fields = ('id', 'register', 'number', 'year', 'color', 'model', 'made')