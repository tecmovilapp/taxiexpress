# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from datetime import datetime

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.utils.encoding import force_text
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth import login

from core.mailer.token import account_activation_token

class CustomClaimsTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomClaimsTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['firstName'] = user.first_name
        token['lastName'] = user.last_name
        token['email'] = user.email
        token['iat'] = int(time.time())
        # ...

        return token

def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return HttpResponse('Gracias por validar su correo. Ahora puede iniciar sesión en el App de Seven.')
    else:
        return HttpResponse('El link de activación no es válido!')

class CustomClaimsTokenObtainPairViewSet(TokenObtainPairView):
    serializer_class = CustomClaimsTokenObtainPairSerializer
