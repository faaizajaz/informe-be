from account.permissions import IsOwner, IsReporter
from base_project.serializers import (
    ItemCreateSerializer,
    ItemUpdateSerializer,
    ItemViewSerializer,
    NestedItemSerializer,
    NestedProjectSerializer,
    OrgCreateSerializer,
    OrgListSerializer,
    OrgMemberEditSerializer,
    OrgOwnerEditSerializer,
    ProjectEditSerializer,
    ProjectListSerializer,
)
from django.db.models import Q
from rest_framework import generics, permissions

from .models import Item, Organization, Project


# class OrgAll
class OrgList(generics.ListAPIView):
    serializer_class = OrgListSerializer
    # TODO: add permissions to OrgList

    def get_queryset(self):
        user = self.request.user
        orgs = Organization.objects.filter(member=user.id)
        return orgs


# To see all projects in an organization
class OrgAllProjects(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    # TODO: Permissions--only available to Org owner

    def get_queryset(self):
        user = self.request.user
        current_org = Organization.objects.get(id=user.current_org)
        projects = Project.objects.filter(organization=current_org)
        return projects


class OrgCreate(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrgCreateSerializer
    # TODO: Figure out who should be able to create organizations

    def perform_create(self, serializer):
        serializer.save(owner=[self.request.user], member=[self.request.user])


class OrgOwnerEdit(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrgOwnerEditSerializer
    # TODO: Only Org Owners can do this


class OrgMemberEdit(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrgMemberEditSerializer


class ProjectList(generics.ListAPIView):
    """
    Provides a list of all projects
    """

    serializer_class = ProjectListSerializer
    permission_classes = [permissions.IsAuthenticated]

    # TODO: Fail gracefully if no user logged in
    def get_queryset(self):
        user = self.request.user
        projects = Project.objects.filter(Q(owner=user) | Q(reporter=user)).distinct()
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
        current_org = Organization.objects.get(id=self.request.user.current_org)
        serializer.save(owner=[self.request.user], organization=current_org)


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
