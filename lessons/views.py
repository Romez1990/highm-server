from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import (
    MethodNotAllowed,
)

from users.permissions import IsStudent
from users.utils import get_n
from .serializers import (
    LessonBasicSerializer,
)
from .lessons import Lessons


class LessonViewSet(ModelViewSet):
    permission_classes = [IsStudent]
    lookup_field = 'number'
    lookup_type = 'int'

    serializer_classes = {
        'list': LessonBasicSerializer,
        'create': Serializer,
        'retrieve': Serializer,
        'update': Serializer,
        'partial_update': Serializer,
        'destroy': Serializer,
    }

    def get_serializer_class(self):
        number = self.kwargs.get('number', None)
        if self.action == 'retrieve':
            return Lessons.get_lesson_serializer_class(number)
        return self.serializer_classes[self.action]

    def get_queryset(self):
        return Lessons.get_list()

    def get_object(self):
        number = self.kwargs['number']
        n = get_n(self.request)
        return Lessons.get_lesson_or_404(number, n)

    def create(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def partial_update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)
