from account.permissions import IsOwner, IsReporter
from django.db.models import Q
from rest_framework import generics, permissions
from serializers.serializers import (
    ItemCreateSerializer,
    ItemUpdateSerializer,
    ItemViewSerializer,
    NestedItemSerializer,
    NestedProjectSerializer,
    ProjectEditSerializer,
    ProjectListSerializer,
)

from .models import Item, Project

# class OrgAll

# class OrgAllProjects

# class OrgCreate
#       Creator of org becomes owner and automatically also becomes a member

# class OrgEdit
#       If a new owner is added, autmatically make a member


class ProjectList(generics.ListAPIView):
    """
    Provides a list of all projects
    """

    serializer_class = ProjectListSerializer
    permission_classes = [permissions.IsAuthenticated]

    # TODO: Fail gracefully if no user logged in
    def get_queryset(self):
        user = self.request.user
        projects = Project.objects.all().filter(Q(owner=user) | Q(reporter=user))
        return projects


# This will work because it uses MPTT, and since only one project Item is linked to one Project,
# it will return a nested JSON with the project at the root.
class ProjectDetail(generics.RetrieveAPIView):
    """
    Provides detail on a specific project. This uses the flat
    "ProjectSerializer" which contains a "depth" parameter,
    so all related objects are visible in this view (Impact,
    Outcome, Output)
    """

    queryset = Project.objects.all()
    serializer_class = NestedProjectSerializer
    permission_classes = [IsOwner | IsReporter]


class ProjectCreate(generics.CreateAPIView):
    """
    Creates a new Project object using the flat serializer. Only
    used to create new impacts, not to define relation to Impacts.
    """

    queryset = Project.objects.all()
    serializer_class = NestedProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # NOTE: arg is a list since 'owner' is an M2M field
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
