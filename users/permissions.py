from rest_framework import permissions
from .models import User
from rest_framework.views import Request, View


class IsProfileOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return obj.id == request.user.id or request.user.is_superuser
