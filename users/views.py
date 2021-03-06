from typing import (
    Type,
)
from django.http import Http404
from rest_framework.generics import (
    GenericAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.serializers import (
    Serializer,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError, MethodNotAllowed
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_auth.registration.views import VerifyEmailView as VerifyEmailViewBase

from .models import (
    Student,
    Teacher,
    Group,
    GROUP_ADMINS,
    UnregisteredUser,
)
from .serializers import (
    ProfileSerializer,
    StudentSerializer,
    TeacherSerializer,
    UnregisteredStudentSerializer,
    UnregisteredTeacherCreateSerializer,
    GroupBasicSerializer,
    GroupCreateSerializer,
    GroupSerializer,
    RegistrationCodeCheckSerializer,
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
            return self.get_serializer_unregistered(*args, **kwargs)
        return self.get_serializer_registered(*args, **kwargs)

    def get_serializer_registered(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class_registered(*args, **kwargs)

    def get_serializer_unregistered(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class_unregistered(*args, **kwargs)

    def list(self, request: Request, **kwargs) -> Response:
        registered_queryset = self.get_queryset_registered()
        registered = self.get_serializer_registered(registered_queryset,
                                                    many=True).data
        unregistered_queryset = self.get_queryset_unregistered()
        unregistered = self.get_serializer_unregistered(unregistered_queryset,
                                                        many=True).data
        return Response(registered + unregistered)

    def create(self, request: Request, **kwargs) -> Response:
        serializer = self.get_serializer_unregistered(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class StudentViewSet(RegistrableModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class_registered = StudentSerializer
    serializer_class_unregistered = UnregisteredStudentSerializer

    def get_queryset_registered(self):
        user = self.request.user
        queryset = Student.objects
        if user.is_superuser:
            return queryset
        return queryset.filter(group__teacher__user=user) \
            .exclude(group__name=GROUP_ADMINS)

    def get_queryset_unregistered(self):
        user = self.request.user
        queryset = UnregisteredUser.objects.filter(is_staff=False)
        if user.is_superuser:
            return queryset
        return queryset.filter(group__teacher__user=user)\
            .exclude(group__name=GROUP_ADMINS)


class TeacherViewSet(RegistrableModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class_registered = TeacherSerializer
    serializer_class_unregistered = UnregisteredTeacherCreateSerializer

    def get_queryset_registered(self):
        return Teacher.objects

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
        user = self.request.user
        queryset = Group.objects
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(teacher__user=user).exclude(name=GROUP_ADMINS)

    def destroy(self, *args, **kwargs) -> Response:
        group = self.get_object()
        if group.students.exists() or group.unregistered_students.exists():
            raise ValidationError({
                'number_of_students': [
                    'Cannot delete non-empty group.',
                ],
            })
        return super().destroy(*args, **kwargs)


class RegistrationCodeCheckView(GenericAPIView):
    serializer_class = RegistrationCodeCheckSerializer

    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'detail': 'Registration code is valid.',
        })


class EmailVerificationKeyCheckView(VerifyEmailViewBase):
    def post(self, request: Request, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        try:
            self.get_object()
        except Http404:
            raise ValidationError({
                'key': ['Invalid verification key.']
            })
        return Response({
            'detail': 'Verification key is valid.',
        })


class VerifyEmailView(VerifyEmailViewBase):
    def get(self, request: Request) -> Response:
        raise MethodNotAllowed(request.method)

    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            super().post(request, *args, **kwargs)
        except Http404:
            raise ValidationError({
                'key': ['Invalid verification key.']
            })
        return Response({
            'detail': 'Email verified.'
        })
