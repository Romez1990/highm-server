from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import (
    ValidationError,
    NotFound,
    MethodNotAllowed,
)

from users.permissions import IsStudent
from users.utils import get_n
from .models import (
    LessonResult,
    TaskResult,
)
from .serializers_for_student import (
    LessonBasicSerializer,
    LessonResultSerializer,
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
        'result': LessonResultSerializer,
    }

    def get_serializer_class(self):
        number = self.kwargs.get('number', None)
        if self.action == 'retrieve':
            return Lessons.get_lesson_serializer_class(number)
        if self.action == 'check':
            return Lessons.get_lesson_answers_serializer_class(number)
        return self.serializer_classes[self.action]

    def get_queryset(self):
        user = self.request.user
        student = user.student
        return Lessons.get_list(student)

    def get_object(self):
        self.check_passed()
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

    @action(detail=True, methods=['post'])
    def check(self, request: Request, number: int) -> Response:
        self.check_passed()
        request_serializer = self.get_serializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        n = get_n(request)
        lesson_answers = Lessons.get_answers_or_404(
            number, n, request_serializer.validated_data)
        lesson_answers.check()
        grade = lesson_answers.grade
        student = request.user.student
        result_queryset = self.result_queryset()
        if result_queryset.exists():
            lesson_result: LessonResult = result_queryset.first()
            lesson_result.grade = grade
            lesson_result.save(update_fields=['grade'])
            TaskResult.objects.filter(lesson_result=lesson_result).delete()
        else:
            lesson_result = LessonResult.objects.create(
                student=student, n=n, lesson_number=number, grade=grade)
        task_results = [
            TaskResult(lesson_result=lesson_result, task_number=task_number,
                       points=answer.points, answer=answer.to_json())
            for task_number, answer in enumerate(lesson_answers.answers, 1)]
        TaskResult.objects.bulk_create(task_results)
        return self.response_lesson_result(lesson_result)

    @action(detail=True, methods=['get'])
    def result(self, request: Request, number: int) -> Response:
        Lessons.lesson_exists_of_404(number)
        self.check_not_passed()
        lesson_result = self.result_queryset().first()
        return self.response_lesson_result(lesson_result)

    def check_passed(self) -> None:
        result_queryset = self.result_queryset()
        if result_queryset.exists() and result_queryset.first().grade != 2:
            raise ValidationError({
                'detail': 'Lesson has been passed.',
            })

    def check_not_passed(self) -> None:
        result_queryset = self.result_queryset()
        if not result_queryset.exists():
            raise ValidationError({
                'detail': 'Lesson has not been passed.',
            })

    def result_queryset(self) -> QuerySet:
        user = self.request.user
        student = user.student
        number = self.kwargs['number']
        return LessonResult.objects.filter(student=student,
                                           lesson_number=number)

    def response_lesson_result(self, lesson_result: LessonResult) -> Response:
        self.action = 'result'
        response_serializer = self.get_serializer(lesson_result)
        return Response(response_serializer.data)
