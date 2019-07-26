from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCreationOrIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return view.action == 'create' or request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return view.action in ['retrieve', 'update', 'partial_update'] and obj.id == request.user.id or request.user.is_staff