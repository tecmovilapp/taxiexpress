
from taxiadmin.models import VehicleAssignment
from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers.vehicle import VehicleSerializer


from taxiadmin.models import Driver, VehicleAssignment, Vehicle


class DriversViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = VehicleSerializer
    queryset = Driver.objects.all()

    @action(detail=True)
    def vehicles(self, request, driver_id=None):
        # driver = Driver.objects.get(id=driver_id)
        # vehicle_ids = VehicleAssignment.objects.filter(driver__id=driver_id).only('id')
        # vehicles = Vehicle.objects.filter(id__in=vehicle_ids)

        

        return []


