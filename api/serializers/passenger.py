


from rest_framework import serializers
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from api.serializers.user import UserSerializer

from core.mailer.email import EmailSender
from core.mailer.token import account_activation_token

from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from taxiadmin.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Passenger
        fields = ('identifier', 'user', 'phone')

    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User(
            email=user_data.get('email'), username=user_data.get('email'),
            first_name=user_data.get('first_name'), last_name=user_data.get('last_name', ''),
            is_active=False)
        user.set_password(user_data.get('password'))
        user.save()
    
        passenger = Passenger.objects.create(user=user,
            identifier=validated_data.get('identifier'), phone=validated_data.get('phone'))

        sender = EmailSender()
        message = {
            'user': user.get_full_name(),
            'domain': get_current_site(self.context.get('request')).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        }
        #sender.send_with_template(i
        #    user.email, 'mailer/activate_account.html', 'Activar su cuenta de Seven.', message)

        html_content = render_to_string('mailer/activate_account.html', message)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives('Activar su cuenta de Seven.', text_content, 'tecmovil.app@gmail.com', [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return passenger


        
