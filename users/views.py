from rest_framework.generics import (
    RetrieveUpdateAPIView,
)
from rest_framework.viewsets import ModelViewSet

from .models import (
    Group,
    GROUP_ADMINS,
)
from .serializers import (
    ProfileSerializer,
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


class GroupViewSet(ModelViewSet):
    permission_classes = [IsTeacher]
    lookup_field = 'name'
    lookup_value_regex = '.+'
    serializer_class = GroupSerializer

    def get_queryset(self):
        queryset = Group.objects
        if self.request.user.is_superuser:
            return queryset
        return queryset.exclude(name=GROUP_ADMINS)
