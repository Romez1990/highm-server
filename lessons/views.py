from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from users.permissions import IsStudent
from users.utils import get_n
from .base import LessonBasicSerializer
from .lessons import Lessons
from .models import (
    LessonResult,
    TaskResult,
)


class LessonViewSet(ViewSet):
    permission_classes = [IsStudent]
    lookup_field = 'number'
    lookup_value_regex = r'\d+'

    def list(self, request: Request) -> Response:
        lessons = Lessons.get_lesson_list()
        serializer = LessonBasicSerializer(lessons, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, number: str) -> Response:
        n = get_n(request)
        lesson = Lessons.get_lesson_or_404(int(number), n)
        serializer = lesson.serializer(lesson)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def check(self, request: Request, number: str) -> Response:
        student = request.user.student
        number_int = int(number)

        queryset = LessonResult.objects.filter(student=student,
                                               lesson_number=number_int)
        if queryset.exists():
            raise ValidationError({
                'detail': 'This lesson has been passed.'
            })

        serializer = Lessons.get_lesson_results_serializer_or_404(
            number_int, data=request.data)
        serializer.is_valid(raise_exception=True)
        n = get_n(request)
        results = serializer.validated_data
        lesson_results = Lessons.get_lesson_results_or_404(number_int, n,
                                                           results)
        check_results = lesson_results.check()

        lesson_result = LessonResult.objects.create(student=student,
                                                    lesson_number=number_int,
                                                    grade=0)
        task_answers = []
        for number, answer in enumerate(results['answers'].values(), 1):
            task_answer = TaskResult(lesson_result=lesson_result,
                                     task_number=number, answer=answer)
            task_answers.append(task_answer)
        TaskResult.objects.bulk_create(task_answers)

        return Response({
            'results': check_results
        })
