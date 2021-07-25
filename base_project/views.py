from .models import Project, Item
from serializers.serializers import (
    ItemCreateSerializer,
    ItemUpdateSerializer,
    NestedItemSerializer,
    NestedProjectSerializer,
    ItemViewSerializer,
    ProjectEditSerializer,
    ProjectListSerializer,
)
from rest_framework import generics, permissions
from account.permissions import IsOwner


class ProjectList(generics.ListAPIView):
    """
    Provides a list of all projects
    """

    serializer_class = ProjectListSerializer
    permission_classes = [permissions.IsAuthenticated]

    # TODO: Fail gracefully if no user logged in
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(owner=user)


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
    serializer_class = NestedProjectSerializer
    permission_classes = [IsOwner]


class ProjectCreate(generics.CreateAPIView):
    """
    Creates a new Project object using the flat serializer. Only
    used to create new impacts, not to define relation to Impacts.
    """

    queryset = Project.objects.all()
    serializer_class = NestedProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=[self.request.user])


class ProjectEdit(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectEditSerializer


class ItemList(generics.ListAPIView):
    queryset = Item.objects.filter(level=0)
    serializer_class = ItemViewSerializer


class ItemEdit(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = NestedItemSerializer


class ItemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCreateSerializer


class ItemDelete(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemUpdateSerializer
