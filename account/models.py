import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from informe_be.settings import PROFILE_PICTURE_MAX_DIM
from PIL import Image


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

    # To resize profile picture on save. This takes center of image.
    def save(self):
        super().save()
        img = Image.open(self.profile_picture.path)

        if img.height > PROFILE_PICTURE_MAX_DIM or img.width > PROFILE_PICTURE_MAX_DIM:
            start_x = (img.width // 2) - (PROFILE_PICTURE_MAX_DIM // 2)
            start_y = (img.height // 2) - (PROFILE_PICTURE_MAX_DIM // 2)
            end_x = (img.width // 2) + (PROFILE_PICTURE_MAX_DIM // 2)
            end_y = (img.height // 2) + (PROFILE_PICTURE_MAX_DIM // 2)

            area = (start_x, start_y, end_x, end_y)
            cropped_img = img.crop(area)
            cropped_img.save(self.profile_picture.path)
