from rest_framework.permissions import BasePermission, IsAuthenticated


class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_superuser


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and request.user.is_staff


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and not request.user.is_staff


def IsOwner(owner_field):
    class Permission(BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.user.is_superuser:
                return True
            if not hasattr(obj, owner_field):
                raise ValueError(
                    f'owner field {owner_field} not found')
            return request.user.is_authenticated and request.user == getattr(obj, owner_field)

    return Permission
