from rest_framework.viewsets import ModelViewSet

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
