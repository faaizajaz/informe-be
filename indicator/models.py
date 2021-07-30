from base_project.models import Item
from django.db import models


class Indicator(models.Model):
    name = models.CharField(
        verbose_name="Name of indicator", max_length=1000, null=True
    )
    description = models.TextField(verbose_name="Description of indicator", null=True)
    item = models.ForeignKey(
        Item,
        verbose_name="Parent item",
        related_name="indicator",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )


class IndicatorEvidence(models.Model):
    name = models.CharField(verbose_name="Name of evidence", max_length=1000, null=True)
    description = models.TextField(verbose_name="Description of evidence", null=True)
    indicator = models.ManyToManyField(Indicator, related_name="evidence", null=True)
    file = models.FileField(verbose_name="Evidence documentation", null=True)
    # TODO: Add reporter field and have it default to request.user
