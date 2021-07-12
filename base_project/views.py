from .models import Project, Item
from serializers.flat_serializers import (
    NestedItemSerializer,
    ProjectSerializer,
    ItemViewSerializer,
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


class ItemList(generics.ListAPIView):
    queryset = Item.objects.filter(level=0)
    serializer_class = ItemViewSerializer


class ItemEdit(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = NestedItemSerializer


class ItemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = NestedItemSerializer
