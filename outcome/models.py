from django.db import models
from intoutcome.models import IntOutcome
from output.models import Output


class Outcome(models.Model):
    short_description = models.CharField(
        verbose_name="Short description of outcome", max_length=1000
    )
    long_description = models.TextField(verbose_name="Long description of outcome")

    # Can link directly to output, or via intermediate outcome
    # TODO: Add something that checks a flag in project for whether intoutcome
    intoutcome = models.ManyToManyField(IntOutcome, null=True, blank=True)
    output = models.ManyToManyField(Output, null=True, blank=True)

    def __str__(self):
        return self.short_description
