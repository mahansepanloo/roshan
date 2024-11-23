from rest_framework.permissions import BasePermission
from rest_framework.exceptions import  PermissionDenied


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_admin or request.user.is_superuser:
            return True
        raise PermissionDenied("Access denied.")