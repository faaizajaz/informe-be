from .models import Project, Item
from serializers.flat_serializers import ProjectSerializer, ItemSerializer
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
    queryset = Item.objects.filter(item_type="Impact")
    serializer_class = ItemSerializer


# class ProjectEdit(generics.UpdateAPIView):
#     """
#     Updates an existing Project object using the nested serializer
#     so can also edit relations to Impact and other objects. This is also
#     used to define initial relations, since we can't do so with
#     the ProjectCreate view as it uses a flat serializer.
#     """

#     queryset = Project.objects.all()
#     serializer_class = NestedProjectSerializer
