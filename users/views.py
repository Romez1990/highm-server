from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.generics import (
    RetrieveUpdateAPIView,
)
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.authentication import TokenAuthentication
from rest_auth.registration.views import (
    RegisterView as BaseRegisterView,
    VerifyEmailView as BaseVerifyEmailView,
)

from .models import (
    Profile,
    Group,
    RegistrationCode,
)
from .serializers import (
    ProfileSerializer,
    GroupSerializer,
    GroupDetailsSerializer,
    RegistrationCodeSerializer,
    RegistrationDetailsCodeSerializer,
    RegistrationCodeListSerializer,
)
from .permissions import IsAuthenticated, IsTeacher


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def get_queryset(self):
        return Profile.objects.none()


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [IsTeacher]
    lookup_field = 'name'
    lookup_value_regex = '.+'
    serializer_classes = {
        'list': GroupSerializer,
        'create': GroupSerializer,
        'retrieve': GroupDetailsSerializer,
        'update': GroupSerializer,
        'partial_update': GroupSerializer,
        'destroy': GroupSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.students.count() or obj.unregistered_students.count():
            raise ValidationError({
                'number_of_students': ['Cannot delete non-empty group.'],
            })
        self.perform_destroy(obj)
        return Response(status=HTTP_204_NO_CONTENT)


class RegistrationCodeViewSet(ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_classes = {
        'list': RegistrationCodeSerializer,
        'create': RegistrationDetailsCodeSerializer,
        'create_list': RegistrationCodeListSerializer,
        'retrieve': RegistrationCodeSerializer,
        'update': RegistrationCodeSerializer,
        'partial_update': RegistrationCodeSerializer,
        'destroy': RegistrationCodeSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_queryset(self):
        return RegistrationCode.objects.filter(group__teacher=self.request.user)

    @action(detail=False, methods=['post'])
    def create_list(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED,
                        headers=headers)


class RegisterView(BaseRegisterView):
    # to avoid csrf failing error
    authentication_classes = [TokenAuthentication]


class VerifyEmailView(BaseVerifyEmailView):
    # to avoid csrf failing error
    authentication_classes = [TokenAuthentication]
