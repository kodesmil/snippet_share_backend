from rest_framework import permissions


class IsOwnerOrReadOnlyCollection(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the collection
        return obj.author == request.user


class IsOwnerOrReadOnlySnippet(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet
        return obj.collection.author == request.user


class IsAdminTag(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the comment
        elif request.method == 'DELETE':
            return request.user.is_superuser is True
        elif request.method == 'POST':
            return True
        else:
            return False
