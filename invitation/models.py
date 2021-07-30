import uuid

from account.models import CustomUser
from base_project.models import Organization
from django.db import models


class OrgInvitation(models.Model):
    sender = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    receiver_email = models.EmailField()
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
