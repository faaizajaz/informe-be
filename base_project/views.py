from account.models import CustomUser
from account.permissions import IsOwner, IsReporter
from account.serializers import UserSerializer
from base_project.serializers import (
    ItemCreateSerializer,
    ItemUpdateSerializer,
    ItemViewSerializer,
    NestedItemSerializer,
    NestedProjectSerializer,
    OrgCreateSerializer,
    OrgMemberEditSerializer,
    OrgOwnerEditSerializer,
    ProjectEditSerializer,
    ProjectListSerializer,
)
from django.db.models import Q
from rest_framework import generics, permissions

from .models import Item, Organization, Project


# To see all projects in an organization
# TODO: Current org needs to be set somewhere.
class OrgAllProjects(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    # TODO: Permissions--only available to Org owner

    def get_queryset(self):
        user = self.request.user
        current_org = Organization.objects.get(id=user.current_org.id)
        projects = Project.objects.filter(organization=current_org)
        return projects


class OrgAllMembers(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        current_org = self.request.user.current_org
        members = CustomUser.objects.filter(org_joined=current_org)
        return members


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
    Provides a list of all projects owned or reported to for the
    current user and the user's current organization
    """

    serializer_class = ProjectListSerializer
    permission_classes = [permissions.IsAuthenticated]

    # TODO: Fail gracefully if no user logged in
    def get_queryset(self):
        user = self.request.user
        projects = Project.objects.filter(
            Q(owner=user) | Q(reporter=user), Q(organization__id=user.current_org)
        ).distinct()
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
        # TODO: Try here to catch user.current_org undefined
        current_org = Organization.objects.get(id=self.request.user.current_org)
        # NOTE: owner arg is a list since it is an M2M field
        serializer.save(
            owner=[self.request.user],
            reporter=[self.request.user],
            organization=current_org,
        )


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
