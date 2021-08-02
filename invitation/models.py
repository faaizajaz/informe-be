import uuid

from account.models import CustomUser
from base_project.models import Organization
from django.db import models


class OrgInvitation(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    receiver_email = models.EmailField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
