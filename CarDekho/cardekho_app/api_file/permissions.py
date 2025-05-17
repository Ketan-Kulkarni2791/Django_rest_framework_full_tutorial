from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """
    Custom permission to only allow admins to edit objects.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user and request.user.is_staff


class ReviewUserPermissionOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow users to edit their own reviews.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user and request.user.is_authenticated