
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

            """return Response(serializer.data, status='200', headers={'access-control-allow-origin ':'*'})"""
            return Response(serializer.data, status='200')
        except Driver.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        try:
            review = request.data["review"]
            obj_driver = Driver.objects.get(user__pk=pk)
            obj_driver.rating = (obj_driver.rating * obj_driver.reviews + review)/(obj_driver.reviews + 1)
            obj_driver.reviews = obj_driver.reviews + 1
            obj_driver.save()

            serializer = DriverSerializer(obj_driver, context={'request': request})

            return Response(None, status='201')
        except Driver.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status='500')

    @action(detail=True, methods=['get'])   
    def rate(self, request, pk=None):
        """Retrieves a driver rate"""

        try:
            obj_driver = Driver.objects.get(user__pk=pk)
            serializer = DriverSerializer(obj_driver, context={'request': request})

            return Response(serializer.data["rating"], status='200')
        except Driver.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)