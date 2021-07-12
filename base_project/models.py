from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Project(models.Model):
    """
    The "Project" component of the project's logical framework. This is the
    highest level component. It defines a O2M relationship to "Impact"
    """

    name = models.CharField(verbose_name="Project name", max_length=500)
    short_description = models.CharField(
        verbose_name="Short description of project", max_length=1000
    )
    long_description = models.TextField(verbose_name="Long description of project")

    # TODO: null should not be allowed in production
    def __str__(self):
        return self.name


class Item(MPTTModel):
    """
    The "Item" component of the project's logical framework. This is the
    lowest level component.
    """

    short_description = models.CharField(
        verbose_name="Short description of Item", max_length=1000
    )
    long_description = models.TextField(verbose_name="Long description of Item")

    parent = TreeForeignKey("self", blank=True, null=True, on_delete=models.DO_NOTHING)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="items")

    item_type = models.CharField(verbose_name="Item type", max_length=500)

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.short_description
