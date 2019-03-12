from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site

from core.mailer.email import EmailSender



@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender:
    :param reset_password_token:
    :param args:
    :param kwargs:
    :return:
    """
    context = {
        'current_user': reset_password_token.user,
        'domain': reset_password_token.ip_address,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key),
        'token': reset_password_token.key
    }
    
    sender = EmailSender()

    sender.send_with_template(
        reset_password_token.user.email, 'reset_password/user_reset_password.html', 'Reset your password.', context)

    print('sent email')
    