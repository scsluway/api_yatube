from rest_framework import permissions


class OnlyAuthorUpdateDestroy(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        method = request.method
        if method == 'DELETE' or method == 'PUT' or method == 'PATCH':
            return obj.author == request.user
        return True
