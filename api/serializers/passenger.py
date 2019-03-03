


from rest_framework import serializers
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from api.serializers.user import UserSerializer

from core.mailer.email import EmailSender
from core.mailer.token import account_activation_token

from taxiadmin.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Passenger
        fields = ('identifier', 'user', 'phone')

    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User(
            email=user_data.get('email'), username=user_data.get('username'),
            first_name=user_data.get('first_name'), last_name=user_data.get('last_name', ''),
            is_active=False)
        user.set_password(user_data.get('password'))
        user.save()
    
        passenger = Passenger.objects.create(user=user,
            identifier=validated_data.get('identifier'), phone=validated_data.get('phone'))

        sender = EmailSender()
        message = {
            'user': user.pk,
            'domain': 'localhost:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        }
        sender.send_with_template(
            user.email, 'mailer/activate_account.html', 'Activate your account.', message)


        return passenger


        