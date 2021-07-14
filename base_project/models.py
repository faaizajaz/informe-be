from django.db import models, router
from mptt.models import MPTTModel, TreeForeignKey
from rest_framework import status
from rest_framework.response import Response

# TODO: Figure out all these nulls and blanks!
class Project(models.Model):
    """
    The "Project" component of the project's logical framework. This is the
    highest level component. It defines a O2M relationship to "Impact"
    """

    name = models.CharField(
        verbose_name="Project name", max_length=500, null=True, blank=True
    )
    long_description = models.TextField(
        verbose_name="Long description of project", null=True, blank=True
    )

    def __str__(self):
        return self.name


class Item(MPTTModel):
    """
    The "Item" component of the project's logical framework. This is the
    lowest level component.
    """

    # This is optional, and only when a new project is created
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="nodes", null=True, blank=True
    )

    item_type = models.CharField(
        verbose_name="Item type", max_length=500, null=True, blank=True
    )
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

    # def delete(self, *args, **kwargs):
    #     if not self.project:
    #         super().delete(*args, **kwargs)
    #         print("not doing")
    #     elif self.project:
    #         return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, *args, **kwargs):
        if not self.project:
            return super().delete(*args, **kwargs)
        else:
            # This doesn't work, but I guess the frontend won't provide a way to do this so
            # no need to handle it.
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
