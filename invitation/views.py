from base_project.models import Organization
from django.core.mail import EmailMessage
from django.http.response import JsonResponse
from informe_be import settings
from rest_framework import generics
from rest_framework.response import Response

from .models import OrgInvitation
from .serializers import OrgInvitationCreateSerializer


class SendOrgInvitation(generics.CreateAPIView):
    queryset = OrgInvitation.objects.all()
    serializer_class = OrgInvitationCreateSerializer

    def post(self, request):
        invitation = OrgInvitation(
            sender=request.data['sender'],
            receiver_email=request.data['receiver_email'],
            organization=request.data['organization'],
        )
        invitation.save()
        to = invitation.receiver_email
        from_email = settings.EMAIL_HOST_USER
        subject = f"Invitation to join {invitation.organization.name}"
        body = (
            "Please click to join:"
            f" https://www.informe.com/api/invitation/accept/{invitation.uid}"
        )

        email = EmailMessage(subject=subject, body=body, from_email=from_email, to=to)
        email.send()

        return Response(status=200)


def handle_org_invitation(request, uid):
    invitation = OrgInvitation.objects.get(uid)
    if invitation:
        if (
            request.user.is_authenticated
            and invitation.receiver_email == request.user.email
        ):
            org = Organization.objects.get(id=invitation.organization.id)
            org.member.add(request.user.id)
            org.save()
            return JsonResponse(
                {'detail': 'Successfully added to organization'}, status=200
            )
        else:
            return JsonResponse(
                {'detail': 'User is not logged in or email mismatch.'}, status=401
            )
    else:
        return JsonResponse({'detail': 'Invitation does not exist.'}, status=404)
