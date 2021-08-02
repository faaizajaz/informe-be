import django.dispatch

org_invitation_received = django.dispatch.Signal(
    providing_args=["notification_receiver", "org", "invitation_sender"]
)

org_invitation_accepted = django.dispatch.Signal(
    providing_args=["notification_receiver", "org", "invitation_receiver"]
)
