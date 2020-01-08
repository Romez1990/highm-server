from rest_framework.generics import (
    RetrieveUpdateAPIView,
)
from rest_framework.viewsets import ModelViewSet

from .models import (
    Profile,
    Group,
)
from .serializers import (
    ProfileSerializer,
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

    def get_queryset(self):
        return Profile.objects.none()


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
