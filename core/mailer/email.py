
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


class EmailSender(object):

    def send_with_template(self, email, template_name, subject, message):
        rendered_message = render_to_string(template_name, message)

        email_message = EmailMessage(
            subject, rendered_message, to=[email]
        )
        email_message.send()
