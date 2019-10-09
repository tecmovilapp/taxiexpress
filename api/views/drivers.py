
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from api.serializers.driver import DriverSerializer


from taxiadmin.models import Driver, Vehicle


class DriversViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = []
    authentication_classes = []

    def retrieve(self, request, pk=None):
        """Retrieves a driver"""

        try:
            obj_driver = Driver.objects.get(user__pk=pk)
            serializer = DriverSerializer(obj_driver, context={'request': request})
            
            
            return Response(serializer.data, status='200', headers={'access-control-allow-origin ':'*'})
        except Driver.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

