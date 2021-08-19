import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    """Custom user model.

    Attributes:
        current_org (Integer): The user's currently active organization
        uid (Uuid): Unique user identifier

    Related Attributes:
        project_reported (Project): m2m - list of projects for which user is a reporter
        project_owned (Project): m2m - list of projects for which user in an owner
        org_joined (Organization): m2m - list of orgs for which user is a member
        org_owned (Organization): m2m - list of orgs for which user is an owner
    """

    current_org = models.IntegerField(
        verbose_name="Last organization active", default=None, null=True, blank=True
    )

    uid = models.UUIDField(default=uuid.uuid4, editable=False)

    profile_picture = models.ImageField(upload_to='profile-pics', null=True, blank=True)

    def __str__(self):
        return self.username
