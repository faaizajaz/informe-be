from .models import Project
from impact.models import Impact
from serializers.flat_serializers import ProjectSerializer, ImpactSerializer
from serializers.nested_serializers import NestedImpactSerializer
from rest_framework import generics


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ImpactDetail(generics.CreateAPIView):
    queryset = Impact.objects.all()
    serializer_class = ImpactSerializer


class ImpactEdit(generics.UpdateAPIView):
    queryset = Impact.objects.all()
    serializer_class = NestedImpactSerializer
