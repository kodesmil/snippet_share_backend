from rest_framework import permissions


class IsAdminOrPostOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        else:
            return request.user.is_superuser is True
