from rest_framework import serializers

from .models import OrgInvitation


class OrgInvitationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgInvitation
        fields = ['sender', 'receiver_email', 'organization']
