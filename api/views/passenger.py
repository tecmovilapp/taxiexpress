from taxiadmin.models import Passenger

from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication

from api.serializers.passenger import PassengerSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Passenger to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [authentication.JWTAuthentication]

    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
