from django.dispatch import receiver
from notification.models import Notification
from notification.signals import org_invitation_accepted, org_invitation_received


@receiver(org_invitation_received)
def create_org_invitation_received_notification(
    sender, notification_receiver, invitation_sender, org, **kwargs
):
    # ALERT: notification_receiver is a SimpleLazyObject, so we can't do e.g. request.user.first_name
    notification = Notification(
        receiver=notification_receiver,
        subject=f"Invitation to join {org.name}",
        message=f"{invitation_sender} has invited you to join {org.name}",
    )
    notification.save()


@receiver(org_invitation_accepted)
def create_org_invitation_accepted_notification(
    sender, notification_receiver, invitation_receiver, org, **kwargs
):
    # Create the new notification object
    notification = Notification(
        receiver=notification_receiver,
        subject=f"{invitation_receiver} has accepted your invitation.",
        message=(
            f"{invitation_receiver} has accepted your invitation to join {org.name}"
        ),
    )
    notification.save()
