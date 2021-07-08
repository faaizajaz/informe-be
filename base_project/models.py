from django.db import models


class Output(models.Model):
    """
    The "Output" component of the project's logical framework. This is the
    lowest level component.
    """

    short_description = models.CharField(
        verbose_name="Short description of output", max_length=1000
    )
    long_description = models.TextField(verbose_name="Long description of output")

    def __str__(self):
        return self.short_description


class Outcome(models.Model):
    """
    The "Outcome" component of the project's logical framework. This is the
    second lowest level component. It defines an M2M relationship to "Output"
    """

    short_description = models.CharField(
        verbose_name="Short description of outcome", max_length=1000
    )
    long_description = models.TextField(verbose_name="Long description of outcome")

    # Can link directly to output, or via intermediate outcome
    # TODO: Add something that checks a flag in project for whether intoutcome
    output = models.ManyToManyField(Output, null=True, blank=True)

    def __str__(self):
        return self.short_description


class Impact(models.Model):
    """
    The "Impact" component of the project's logical framework. This is the
    second highest level component. It defines an M2M relationship to "Outcome"
    """

    short_description = models.CharField(
        verbose_name="Short description of impact",
        max_length=1000,
        blank=True,
        null=True,
    )
    long_description = models.TextField(
        verbose_name="Long description of impact", blank=True, null=True
    )

    outcome = models.ManyToManyField(Outcome, blank=True, null=True)

    def __str__(self):
        return self.short_description


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
    impact = models.ManyToManyField(Impact, blank=True, null=True)

    def __str__(self):
        return self.name
