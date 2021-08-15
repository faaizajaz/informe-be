from django.core.mail import EmailMessage
from informe_be import settings


def send_email(to: str, subject: str, body: str) -> None:
    """Sends an email message.

    Args:
        to (str): Email address to send message to
        subject (str): Subject of the message
        body (str): Body text of the message
    """
    from_email = settings.EMAIL_HOST_USER

    email = EmailMessage(subject=subject, body=body, from_email=from_email, to=to)
    email.send()
