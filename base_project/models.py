from account.models import CustomUser
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from rest_framework import status
from rest_framework.response import Response


# TODO: Figure out all these nulls and blanks!
# TODO: Figure out all the on_deletes!!!
class Organization(models.Model):
    name = models.CharField(verbose_name="Organization name", max_length=1000)
    description = models.TextField(verbose_name="Organization description")
    owner = models.ManyToManyField(
        CustomUser, verbose_name="Organization owner", related_name="org_owned"
    )
    member = models.ManyToManyField(
        CustomUser, verbose_name="Members", related_name="org_joined"
    )

    profile_picture = models.ImageField(
        upload_to='org_profile-pics', null=True, blank=True
    )

    # ##### RELATED FIELDS ##### #
    # project
    #   TO: Project
    #   TYPE: ForeignKey (1 Org to many Projects)

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    The "Project" component of the project's logical framework. This is a
    container for the project logframe. The root level of the logframe
    is a single Item object with item_type="project".

    """

    name = models.CharField(
        verbose_name="Project name", max_length=500, null=True, blank=True
    )
    long_description = models.TextField(
        verbose_name="Long description of project", null=True, blank=True
    )

    level_config = models.JSONField(null=True, blank=True)

    owner = models.ManyToManyField(CustomUser, related_name='project_owned')

    reporter = models.ManyToManyField(
        CustomUser, related_name='project_reported', null=True, blank=True
    )
    organization = models.ForeignKey(
        Organization,
        related_name="project",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # TODO: Change this initial config

        initial_level_config = [{"level": 0, "name": "Project", "color": "#3399cc"}]

        if not self.level_config:

            self.level_config = initial_level_config
            super().save(*args, **kwargs)

            # ALERT: This assumes that a project without an initial level config also doesn't have a base Item
            project_item = Item(
                project=self,
                is_project=True,
                name=self.name,
                long_description=self.long_description,
            )

            project_item.save()
        else:
            super().save(*args, **kwargs)


class Item(MPTTModel):
    """
    The "Item" component of the project's logical framework. This is a recursive
    component
    """

    # This is optional, and only when a new project is created
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="nodes", null=True, blank=True
    )

    # item_type = models.CharField(
    #     verbose_name="Item type", max_length=500, null=True, blank=True
    # )
    is_project = models.BooleanField(default=False)
    name = models.CharField(
        verbose_name="name of Item", max_length=1000, null=True, blank=True
    )
    long_description = models.TextField(
        verbose_name="Long description of Item", null=True, blank=True
    )

    parent = TreeForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if not self.is_project:
            return super().delete(*args, **kwargs)
        else:
            # NOTE: Not actually allowed to return Response. Still returns 202. Doesn't matter though.
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def save(self, *args, **kwargs):
        if self.parent:
            self.project = self.parent.project
        super().save(*args, **kwargs)
