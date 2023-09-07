from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """
    Custom Permission class
    List, Create, Retrieve : anyone logged in
    Update, Partial update : author or staff
    Destroy : staff only
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve', 'create']:
            return request.user.is_authenticated
        elif view.action in ['update', 'partial_update']:
            return (obj.author == request.user) or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False
