from account.models import CustomUser
from base_project.models import Organization
from base_project.views import OrgAllProjects
from django.core.mail import EmailMessage
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from informe_be import settings
from notification.signals import org_invitation_accepted, org_invitation_received
from rest_framework import generics
from rest_framework.response import Response
from utilities.email import send_email

from .models import OrgInvitation
from .serializers import OrgInvitationCreateSerializer


class SendOrgInvitation(generics.CreateAPIView):
    queryset = OrgInvitation.objects.all()
    serializer_class = OrgInvitationCreateSerializer

    def post(self, request):
        org = Organization.objects.get(id=request.data['organization'])
        invitation = OrgInvitation(
            sender=request.user,
            receiver_email=request.data['receiver_email'],
            organization=org,
        )
        invitation.save()
        to = (invitation.receiver_email,)
        subject = f"Invitation to join {invitation.organization.name}"
        # PREDEPLOY: Change the invitation URL
        body = (
            "Please click to join:"
            f" https://www.informe.com/api/invitation/accept/{invitation.uid}"
        )

        send_email(to, subject, body)

        # CREATE NOTIFICATION TO INVITATION RECEIVER
        try:
            notification_receiver = CustomUser.objects.get(
                email=invitation.receiver_email
            )
            notification_invitation_sender = request.user

            # TODO: Rethink "sender"
            org_invitation_received.send(
                sender=invitation,
                notification_receiver=notification_receiver,
                org=org,
                invitation_sender=notification_invitation_sender,
            )
        except CustomUser.DoesNotExist:
            pass

        return Response(status=200)


@require_POST
def handle_org_invitation(request, uid):
    invitation = OrgInvitation.objects.get(uid=uid)
    if invitation:
        if (
            request.user.is_authenticated
            and invitation.receiver_email == request.user.email  # noqa: W503
        ):
            org = Organization.objects.get(id=invitation.organization.id)
            org.member.add(request.user.id)
            org.save()

            # CREATE NOTIFICATION TO INVITATION SENDER
            # TODO: Rethink "sender"
            org_invitation_accepted.send(
                sender=invitation,
                notification_receiver=invitation.sender,
                invitation_receiver=request.user,
                org=org,
            )

            invitation.delete()

            return JsonResponse(
                {'detail': 'Successfully added to organization'}, status=200
            )
        else:
            return JsonResponse(
                {'detail': 'User is not logged in or email mismatch.'}, status=401
            )
    else:
        return JsonResponse({'detail': 'Invitation does not exist.'}, status=404)
