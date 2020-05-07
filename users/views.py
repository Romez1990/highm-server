from typing import Type
from rest_framework.generics import (
    RetrieveUpdateAPIView,
)
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.authentication import TokenAuthentication
from rest_auth.registration.views import (
    RegisterView as BaseRegisterView,
    VerifyEmailView as BaseVerifyEmailView,
)

from .models import (
    Profile,
    Student,
    Teacher,
    Group,
    UnregisteredUser,
)
from .serializers import (
    ProfileSerializer,
    StudentSerializer,
    TeacherSerializer,
    GroupBasicSerializer,
    GroupCreateSerializer,
    GroupSerializer,
    UnregisteredStudentSerializer,
    UnregisteredTeacherCreateSerializer,
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
    serializer_class_registered: Type[Serializer]
    serializer_class_unregistered: Type[Serializer]

    def get_queryset_registered(self):
        raise NotImplementedError

    def get_queryset_unregistered(self):
        raise NotImplementedError

    def is_registered(self) -> bool:
        pk = self.kwargs['pk']
        return pk[0] != 'c'

    def get_queryset(self):
        # django rest framework call this with rendering list without pk
        if 'pk' in self.kwargs and not self.is_registered():
            return self.get_queryset_unregistered()
        return self.get_queryset_registered()

    def get_serializer(self, *args, **kwargs):
        # django rest framework call this with rendering list without pk
        if 'pk' in self.kwargs and not self.is_registered():
            return self.serializer_class_unregistered(*args, **kwargs)
        return self.serializer_class_registered(*args, **kwargs)

    def list(self, request: Request, **kwargs) -> Response:
        registered_queryset = self.get_queryset_registered()
        registered = self.serializer_class_registered(registered_queryset,
                                                      many=True).data
        unregistered_queryset = self.get_queryset_unregistered()
        unregistered = self.serializer_class_unregistered(unregistered_queryset,
                                                          many=True).data
        return Response(registered + unregistered)

    def create(self, request: Request, **kwargs) -> Response:
        serializer = self.serializer_class_unregistered(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def destroy(self, *args, **kwargs) -> Response:
        if self.is_registered():
            raise ValidationError({
                'non_field_errors': [
                    'Cannot delete a registered user.'
                ]
            })
        return super().destroy(*args, **kwargs)


class StudentViewSet(RegistrableModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class_registered = StudentSerializer
    serializer_class_unregistered = UnregisteredStudentSerializer

    def get_queryset_registered(self):
        user = self.request.user
        if user.is_superuser:
            return Student.objects.all()
        return Student.objects.filter(user__is_superuser=False)

    def get_queryset_unregistered(self):
        return UnregisteredUser.objects.filter(is_staff=False)


class TeacherViewSet(RegistrableModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class_registered = TeacherSerializer
    serializer_class_unregistered = UnregisteredTeacherCreateSerializer

    def get_queryset_registered(self):
        return Teacher.objects.all()

    def get_queryset_unregistered(self):
        return UnregisteredUser.objects.filter(is_staff=True)


class GroupViewSet(ModelViewSet):
    permission_classes = [IsTeacher]
    lookup_field = 'name'
    lookup_value_regex = '.+'
    serializer_classes = {
        'list': GroupBasicSerializer,
        'create': GroupCreateSerializer,
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
        if group.students.exists() or group.unregistered_students.exists():
            raise ValidationError({
                'number_of_students': [
                    'Cannot delete non-empty group.',
                ],
            })
        return super().destroy(*args, **kwargs)


class RegisterView(BaseRegisterView):
    # to avoid csrf failing error
    authentication_classes = [TokenAuthentication]


class VerifyEmailView(BaseVerifyEmailView):
    # to avoid csrf failing error
    authentication_classes = [TokenAuthentication]
