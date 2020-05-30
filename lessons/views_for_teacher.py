from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.exceptions import (
    NotFound,
    MethodNotAllowed,
)

from users.models import (
    Group,
    GROUP_ADMINS,
)
from users.permissions import IsTeacher
from .lessons import LessonsForTeacher
from .models import LessonResult
from .serializers_for_teacher import (
    LessonBasicSerializer,
    LessonResultSerializer, LessonResultAnswersSerializer,
)


class TeacherLessonViewSet(ModelViewSet):
    permission_classes = [IsTeacher]

    serializer_classes = {
        'list': LessonBasicSerializer,
        'create': Serializer,
        'retrieve': Serializer,
        'update': Serializer,
        'partial_update': Serializer,
        'destroy': Serializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_queryset(self):
        return LessonsForTeacher.get_list()

    def create(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def partial_update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)


class LessonResultViewSet(ModelViewSet):
    permission_classes = [IsTeacher]

    serializer_classes = {
        'list': LessonResultSerializer,
        'create': Serializer,
        'retrieve': LessonResultAnswersSerializer,
        'update': Serializer,
        'partial_update': Serializer,
        'destroy': Serializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_queryset(self) -> QuerySet:
        group = self.get_group()
        lesson = self.get_lesson()
        return LessonResult.objects.filter(student__group=group,
                                           lesson_number=lesson)

    def get_object(self) -> LessonResult:
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        return queryset.get(pk=pk)

    def create(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def partial_update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def get_group(self) -> Group:
        user = self.request.user
        queryset = Group.objects
        if not user.is_superuser:
            queryset = queryset.exclude(name=GROUP_ADMINS)

        group = self.kwargs['group']
        queryset = queryset.filter(name=group)

        if not queryset.exists():
            raise NotFound('Group not found.')
        return queryset.first()

    def get_lesson(self) -> int:
        lesson = self.kwargs['lesson']
        LessonsForTeacher.lesson_exists_of_404(lesson)
        return lesson
