# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomClaimsTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomClaimsTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['firstName'] = user.first_name
        token['lastName'] = user.last_name
        token['email'] = user.email
        # ...

        return token

class CustomClaimsTokenObtainPairViewSet(TokenObtainPairView):
    serializer_class = CustomClaimsTokenObtainPairSerializer
