from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.owner.all()


class IsReporter(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.reporter.all()


# TODO: Need an IsOrgOwner permission here
