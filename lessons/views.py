from django.db.models import QuerySet
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
from .serializers import LessonResultSerializer
from .utils.grade import get_grade


class LessonViewSet(ViewSet):
    permission_classes = [IsStudent]
    lookup_field = 'number'
    lookup_value_regex = r'\d+'

    def list(self, request: Request) -> Response:
        student = request.user.student
        lessons = Lessons.get_lesson_list(student)
        serializer = LessonBasicSerializer(lessons, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, number: str) -> Response:
        self.check_lesson_not_passed()

        number_int = int(number)
        n = get_n(request)
        lesson = Lessons.get_lesson_or_404(number_int, n)
        serializer = lesson.serializer(lesson)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def check(self, request: Request, number: str) -> Response:
        self.check_lesson_not_passed()

        number_int = int(number)
        serializer = Lessons.get_lesson_answers_serializer_or_404(
            number_int, data=request.data)
        serializer.is_valid(raise_exception=True)
        n = get_n(request)
        answers = serializer.validated_data
        lesson_answers = Lessons.get_lesson_answers_or_404(number_int, n,
                                                           answers)
        check_results = lesson_answers.check()

        bin_check_results = [1 if result else 0
                             for result in check_results.values()]
        percent_right = sum(bin_check_results) / len(bin_check_results)
        grade = get_grade(percent_right)

        student = request.user.student
        lesson_result = LessonResult.objects.create(student=student,
                                                    lesson_number=number_int,
                                                    grade=grade)
        task_answers = []
        for number, answer_key in enumerate(answers['answers'], 1):
            answer = answers['answers'][answer_key]
            right = check_results[answer_key]
            task_answer = TaskResult(
                lesson_result=lesson_result, task_number=number, right=right,
                answer=answer)
            task_answers.append(task_answer)
        TaskResult.objects.bulk_create(task_answers)

        return Response({
            'results': check_results
        })

    @action(detail=True, methods=['get'])
    def results(self, request: Request, number: str) -> Response:
        self.check_lesson_passed()
        student = request.user.student
        number_int = int(number)
        results = LessonResult.objects.get(student=student,
                                           lesson_number=number_int)
        serializer = LessonResultSerializer(results)
        return Response(serializer.data)

    def check_lesson_not_passed(self) -> None:
        queryset = self.get_queryset()
        if queryset.exists():
            raise ValidationError({
                'detail': 'This lesson has been passed.'
            })

    def check_lesson_passed(self) -> None:
        queryset = self.get_queryset()
        if not queryset.exists():
            raise ValidationError({
                'detail': 'No results for this lesson.'
            })

    def get_queryset(self) -> QuerySet:
        student = self.request.user.student
        number_int = int(self.kwargs['number'])
        return LessonResult.objects.filter(student=student,
                                           lesson_number=number_int)
