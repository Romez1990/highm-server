from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import (
    Group,
)
from .serializers import (
    GroupSerializer,
)
from .permissions import IsTeacher


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
