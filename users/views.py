from rest_framework.generics import (
    RetrieveUpdateAPIView,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import (
    Student,
    Group,
    GROUP_ADMINS,
)
from .serializers import (
    ProfileSerializer,
    StudentSerializer,
    GroupBasicSerializer,
    GroupSerializer,
)
from .permissions import (
    IsAuthenticated,
    IsTeacher,
)


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class RegistrableModelViewSet(ModelViewSet):
    def destroy(self, *args, **kwargs) -> Response:
        raise ValidationError({
            'non_field_errors': [
                'Cannot delete a registered user.'
            ]
        })


class StudentViewSet(RegistrableModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Student.objects
        if user.is_superuser:
            return queryset
        return queryset.exclude(group__name=GROUP_ADMINS)


class GroupViewSet(ModelViewSet):
    permission_classes = [IsTeacher]
    lookup_field = 'name'
    lookup_value_regex = '.+'
    serializer_classes = {
        'list': GroupBasicSerializer,
        'create': GroupBasicSerializer,
        'retrieve': GroupSerializer,
        'update': GroupBasicSerializer,
        'partial_update': GroupBasicSerializer,
        'destroy': GroupBasicSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_queryset(self):
        queryset = Group.objects
        if self.request.user.is_superuser:
            return queryset
        return queryset.exclude(name=GROUP_ADMINS)

    def destroy(self, *args, **kwargs) -> Response:
        group = self.get_object()
        if group.students.exists():
            raise ValidationError({
                'number_of_students': [
                    'Cannot delete non-empty group.',
                ],
            })
        return super().destroy(*args, **kwargs)
