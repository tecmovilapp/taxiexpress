from taxiadmin.models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    register = serializers.CharField(allow_null=True)
    number = serializers.CharField(allow_null=True)
    year = serializers.CharField(allow_null=True)


    class Meta:
        model = Vehicle
        fields = ('id', 'register', 'number', 'year',)