from django.http import Http404
from rest_framework.generics import (
    GenericAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError, MethodNotAllowed
from rest_framework.request import Request
from rest_framework.response import Response
from rest_auth.registration.views import VerifyEmailView as VerifyEmailViewBase

from .models import (
    Student,
    Teacher,
    Group,
    GROUP_ADMINS,
)
from .serializers import (
    ProfileSerializer,
    StudentSerializer,
    TeacherSerializer,
    GroupBasicSerializer,
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


class TeacherViewSet(RegistrableModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects


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
        raise MethodNotAllowed('GET')

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
