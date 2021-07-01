from django.db import models


class Project(models.Model):
    name = models.CharField(verbose_name="Project name", max_length=500)
    short_description = models.CharField(
        verbose_name="Short description of project", max_length=1000
    )
    long_description = models.TextField(verbose_name="Long description of project")
