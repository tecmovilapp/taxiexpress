
from django.contrib.auth.models import User

from taxiadmin.models import VehicleAssignment
from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

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

        try:
            obj_driver = Driver.objects.get(user__pk=pk)
            
            vehicle_list = VehicleAssignment.objects.filter(driver__pk=obj_driver.pk)
            vehicle_driver = {}


            if len(vehicle_list) == 0:
                return Response(None, status=status.HTTP_404_NOT_FOUND)
            
            vehicle_driver = vehicle_list[0]
            
            setattr(obj_driver, 'vehicle', vehicle_driver.vehicle)
            serializer = DriverSerializer(obj_driver, context={'request': request})
            
            
            return Response(serializer.data)
        except Driver.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

