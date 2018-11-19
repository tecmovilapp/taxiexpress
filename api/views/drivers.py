
from django.contrib.auth.models import User

from taxiadmin.models import VehicleAssignment
from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from api.serializers.driver import DriverSerializer


from taxiadmin.models import Driver, VehicleAssignment, Vehicle


class DriversViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [authentication.JWTAuthentication]

    def retrieve(self, request, pk=None):
        """Retrieves a driver"""

        obj_driver = Driver.objects.get(user__pk=pk)
        serializer = DriverSerializer(obj_driver, context={'request': request})
        
        return Response(serializer.data)

    

