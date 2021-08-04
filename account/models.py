from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    current_org = models.IntegerField(
        verbose_name="Last organization active", default=None, null=True, blank=True
    )
    # ##### RELATED FIELDS ##### #
    # project_reported
    #   TO: Project
    #   TYPE: M2M
    #
    # project_owned
    #   TO: Project
    #   TYPE: M2M
    #
    # org_joined
    #   TO: Organization
    #   TYPE: M2M
    #
    # org_owned
    #   TO: Organization
    #   TYPE: M2M

    def __str__(self):
        return self.username
