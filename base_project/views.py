from rest_framework.response import Response
from .models import Project, Item
from serializers.flat_serializers import (
    NestedItemSerializer,
    ProjectSerializer,
    ItemViewSerializer,
)
from rest_framework import generics, status


class ProjectList(generics.ListCreateAPIView):
    """
    Provides a list of all projects
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# This will work because it uses MPTT, and since only one project Item is linked to one Project,
# it will return a nested JSON with the project at the root.
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

    # TODO: Add logic to create a corresponding project item_type Item when project create

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        x = serializer.save()
        project_item = Item(
            project=x,
            item_type="Project",
            name=x.name,
            long_description=x.long_description,
        )
        project_item.save()
        # self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class ItemList(generics.ListAPIView):
    queryset = Item.objects.filter(level=0)
    serializer_class = ItemViewSerializer


class ItemEdit(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = NestedItemSerializer


class ItemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = NestedItemSerializer
