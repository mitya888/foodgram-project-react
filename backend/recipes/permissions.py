from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and (
                request.user.is_superuser
                or obj.author == request.user
                or request.method == 'POST'
        ):
            return True
        return request.method in SAFE_METHODS
