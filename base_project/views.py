from .models import Outcome, Output, Project, Impact
from serializers.flat_serializers import (
    OutcomeSerializer,
    OutputSerializer,
    ProjectSerializer,
    ImpactSerializer,
)
from serializers.nested_serializers import (
    NestedImpactSerializer,
    NestedOutcomeSerializer,
    NestedProjectSerializer,
)
from rest_framework import generics


class ProjectList(generics.ListCreateAPIView):
    """
    Provides a list of all projects
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides detail on a specific project. This uses the flat
    "ProjectSerializer" which contains a "depth" parameter,
    so all related objects are visible in this view (Impact,
    Outcome, Output)
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreate(generics.CreateAPIView):
    """
    Creates a new Project object using the flat serializer. Only
    used to create new impacts, not to define relation to Impacts.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectEdit(generics.UpdateAPIView):
    """
    Updates an existing Project object using the nested serializer
    so can also edit relations to Impact and other objects. This is also
    used to define initial relations, since we can't do so with
    the ProjectCreate view as it uses a flat serializer.
    """

    queryset = Project.objects.all()
    serializer_class = NestedProjectSerializer


class ImpactCreate(generics.CreateAPIView):
    """
    Creates a new Impact object using the flat serializer. Only
    used to create new impacts, not to define relation to Outcome.
    """

    queryset = Impact.objects.all()
    serializer_class = ImpactSerializer


class ImpactEdit(generics.UpdateAPIView):
    """
    Updates an existing Impact object using the nested serializer
    so can also edit relations to Outcome objects. This is also
    used to define initial relations, since we can't do so with
    the ImpactCreate view as it uses a flat serializer.
    """

    queryset = Impact.objects.all()
    serializer_class = NestedImpactSerializer


class ImpactDelete(generics.DestroyAPIView):
    """
    Delete an existing Impact object using the flat serializer.
    """

    queryset = Impact.objects.all()
    serializer_class = ImpactSerializer


class OutcomeCreate(generics.CreateAPIView):
    """
    Creates a new Outcome object using the flat serializer. Only
    used to create new Outcomes, not to define relation to Output.
    """

    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer


class OutcomeEdit(generics.UpdateAPIView):
    """
    Updates an existing Outcome object using the nested serializer
    so can also edit relations to Output objects. This is also
    used to define initial relations, since we can't do so with
    the OutcomeCreate view as it uses a flat serializer.
    """

    queryset = Outcome.objects.all()
    serializer_class = NestedOutcomeSerializer


class OutputCreate(generics.CreateAPIView):
    """
    Creates a new Output object using the flat serializer.
    """

    queryset = Output.objects.all()
    serializer_class = OutputSerializer


class OutputEdit(generics.UpdateAPIView):
    """
    Edit an existing Output object using the flat serializer.
    """

    queryset = Output.objects.all()
    serializer_class = OutputSerializer


class OutputDelete(generics.DestroyAPIView):
    """
    Delete an existing Output object using the flat serializer.
    """

    queryset = Output.objects.all()
    serializer_class = OutputSerializer
