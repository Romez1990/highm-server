from rest_framework.generics import (
    RetrieveUpdateAPIView,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from .models import (
    Profile,
    Student,
    Teacher,
    Group,
)
from .serializers import (
    ProfileSerializer,
    StudentSerializer,
    TeacherSerializer,
    GroupBasicSerializer,
    GroupSerializer,
)
from .permissions import (
    IsAuthenticated,
    IsTeacher,
    IsAdmin,
)


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def get_queryset(self):
        return Profile.objects.none()


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
    queryset = Student.objects.filter(user__is_superuser=False)


class TeacherViewSet(RegistrableModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


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
        if self.request.user.is_superuser:
            return Group.objects.all()
        return Group.objects.all().exclude(name='admins')

    def destroy(self, *args, **kwargs) -> Response:
        group = self.get_object()
        if group.students.count() > 0:
            raise ValidationError({
                'number_of_students': [
                    'Cannot delete non-empty group.',
                ],
            })
        return super().destroy(*args, **kwargs)
