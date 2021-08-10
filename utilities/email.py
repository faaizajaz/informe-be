from django.core.mail import EmailMessage
from informe_be import settings


def send_email(to, subject, body):
    """
    Sends an email
    """
    from_email = settings.EMAIL_HOST_USER

    email = EmailMessage(subject=subject, body=body, from_email=from_email, to=to)
    email.send()
