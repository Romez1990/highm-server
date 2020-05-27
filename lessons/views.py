from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import (
    MethodNotAllowed,
)

from users.permissions import IsStudent


class LessonViewSet(ModelViewSet):
    permission_classes = [IsStudent]

    serializer_classes = {
        'list': Serializer,
        'create': Serializer,
        'retrieve': Serializer,
        'update': Serializer,
        'partial_update': Serializer,
        'destroy': Serializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def list(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def create(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def partial_update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)
