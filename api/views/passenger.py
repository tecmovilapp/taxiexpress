from taxiadmin.models import Passenger

from rest_framework import viewsets, permissions, mixins
from rest_framework_simplejwt import authentication
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from api.serializers.passenger import PassengerSerializer



class PassengerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Passenger to be viewed or edited.
    """
    permission_classes = []
    authentication_classes = []

    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

        
    def retrieve(self, request, pk=None):
        queryset = Passenger.objects.all()
        user = get_object_or_404(queryset, user__id=pk)
        serializer = PassengerSerializer(user)
        return Response(serializer.data)
