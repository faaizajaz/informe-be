from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# TODO: Figure out all these nulls and blanks!
class Project(models.Model):
    """
    The "Project" component of the project's logical framework. This is the
    highest level component. It defines a O2M relationship to "Impact"
    """

    name = models.CharField(
        verbose_name="Project name", max_length=500, null=True, blank=True
    )
    short_description = models.CharField(
        verbose_name="Short description of project",
        max_length=1000,
        null=True,
        blank=True,
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

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="items", null=True, blank=True
    )
    item_type = models.CharField(
        verbose_name="Item type", max_length=500, null=True, blank=True
    )
    short_description = models.CharField(
        verbose_name="Short description of Item", max_length=1000, null=True, blank=True
    )
    long_description = models.TextField(
        verbose_name="Long description of Item", null=True, blank=True
    )

    parent = TreeForeignKey("self", blank=True, null=True, on_delete=models.DO_NOTHING)

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.short_description
