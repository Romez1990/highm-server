from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    RetrieveUpdateAPIView,
)
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import (
    Profile,
    Group,
)
from .serializers import (
    ProfileSerializer,
    GroupSerializer,
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
    serializer_class = GroupSerializer
    permission_classes = [IsTeacher]
    lookup_field = 'name'
    lookup_value_regex = '.+'

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.students.count() or obj.unregistered_students.count():
            raise ValidationError({
                'number_of_students': ['Cannot delete non-empty group.'],
            })
        self.perform_destroy(obj)
        return Response(status=HTTP_204_NO_CONTENT)
