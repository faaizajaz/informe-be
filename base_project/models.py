from django.db import models
from impact.models import Impact


class Project(models.Model):
    name = models.CharField(verbose_name="Project name", max_length=500)
    short_description = models.CharField(
        verbose_name="Short description of project", max_length=1000
    )
    long_description = models.TextField(verbose_name="Long description of project")

    # TODO: null should not be allowed in production
    impact = models.OneToOneField(Impact, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
