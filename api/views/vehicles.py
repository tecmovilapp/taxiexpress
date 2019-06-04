
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from api.serializers.driver import VehicleSerializer

from taxiadmin.models import Vehicle

class VehiclesViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = []
    authentication_classes = []
    def list(self, request):
        queryset = Vehicle.objects.all()
        serializer = VehicleSerializer(queryset, many=True)
        return Response(serializer.data)

