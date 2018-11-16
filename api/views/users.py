from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication

from api.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [authentication.JWTAuthentication]

    queryset = User.objects.all()
    serializer_class = UserSerializer
