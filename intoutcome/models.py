from django.db import models
from output.models import Output


class IntOutcome(models.Model):
    short_description = models.CharField(
        verbose_name="Short description of intermediate outcome", max_length=1000
    )
    long_description = models.TextField(
        verbose_name="Long description of intermediate outcome"
    )

    # Can only link to output
    output = models.ManyToManyField(Output)

    def __str__(self):
        return self.short_description
