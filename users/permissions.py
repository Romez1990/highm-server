from typing import Callable
from django.db.models import Model
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.request import Request

from users.models import User


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


class IsOwner:
    def __new__(cls, get_object_owner: Callable[[Model], User]):
        class Permission(BasePermission):
            def has_object_permission(self, request: Request, view: APIView,
                                      obj: Model) -> bool:
                if request.user.is_superuser:
                    return True
                if not request.user.is_authenticated:
                    return False
                return request.user == get_object_owner(obj)

        return Permission
