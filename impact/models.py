from django.db import models
from outcome.models import Outcome


class Impact(models.Model):

    short_description = models.CharField(
        verbose_name="Short description of impact", max_length=1000
    )
    long_description = models.TextField(verbose_name="Long description of impact")

    outcome = models.ManyToManyField(Outcome)

    def __str__(self):
        return self.short_description
