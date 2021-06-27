from django.db import models


class Output(models.Model):
    short_description = models.CharField(
        verbose_name="Short description of output", max_length=1000
    )
    long_description = models.TextField(verbose_name="Long description of output")
