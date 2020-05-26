from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import (
    ValidationError,
    NotFound,
    MethodNotAllowed,
)

from users.permissions import IsStudent, IsTeacher
from users.models import Group, GROUP_ADMINS
from users.utils import get_n
from .base import (
    LessonBasicSerializer,
)
from .lessons import Lessons
from .models import (
    LessonResult,
    TaskResult,
)
from .serializers import (
    LessonForTeacherSerializer,
    LessonResultForStudentSerializer,
    LessonResultForStatementSerializer,
    LessonResultForStatementAnswersSerializer,
)
from .utils.grade import get_grade


class LessonViewSet(ViewSet):
    permission_classes = [IsStudent]
    lookup_field = 'number'
    lookup_type = 'int'

    def list(self, request: Request) -> Response:
        student = request.user.student
        lessons = Lessons.get_lesson_list_for_student(student)
        serializer = LessonBasicSerializer(lessons, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, number: int) -> Response:
        self.check_lesson_not_passed()

        n = get_n(request)
        lesson = Lessons.get_lesson_or_404(number, n)
        serializer = lesson.serializer(lesson)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def check(self, request: Request, number: int) -> Response:
        self.check_lesson_not_passed()

        serializer = Lessons.get_lesson_answers_serializer_or_404(
            number, data=request.data)
        serializer.is_valid(raise_exception=True)
        n = get_n(request)
        answers = serializer.validated_data
        lesson_answers = Lessons.get_lesson_answers_or_404(number, n, answers)
        check_results = lesson_answers.check()

        bin_check_results = [1 if result else 0
                             for result in check_results.values()]
        percent_correct = round(
            sum(bin_check_results) / len(bin_check_results) * 100)
        grade = get_grade(percent_correct)

        student = request.user.student
        lesson_result = LessonResult.objects.create(
            student=student, lesson_number=number, n=n,
            percent_correct=percent_correct, grade=grade)
        task_answers = []
        for number, answer_key in enumerate(answers['answers'], 1):
            answer = answers['answers'][answer_key]
            correct = check_results[answer_key]
            task_answer = TaskResult(
                lesson_result=lesson_result, task_number=number,
                correct=correct, answer=answer)
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
        serializer = LessonResultForStudentSerializer(results)
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
            raise NotFound('No results found.')

    def get_queryset(self) -> QuerySet:
        student = self.request.user.student
        number_int = int(self.kwargs['number'])
        return LessonResult.objects.filter(student=student,
                                           lesson_number=number_int)


class LessonForTeacherViewSet(ModelViewSet):
    permission_classes = [IsTeacher]

    serializer_classes = {
        'list': LessonForTeacherSerializer,
        'create': LessonForTeacherSerializer,
        'retrieve': LessonForTeacherSerializer,
        'update': LessonForTeacherSerializer,
        'partial_update': LessonForTeacherSerializer,
        'destroy': LessonForTeacherSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_queryset(self):
        return Lessons.get_lesson_list_for_teacher()

    def get_object(self):
        return ...


class StatementViewSet(ModelViewSet):
    permission_classes = [IsTeacher]

    serializer_classes = {
        'list': LessonResultForStatementSerializer,
        'create': LessonResultForStatementAnswersSerializer,
        'retrieve': LessonResultForStatementAnswersSerializer,
        'update': LessonResultForStatementAnswersSerializer,
        'partial_update': LessonResultForStatementAnswersSerializer,
        'destroy': LessonResultForStatementAnswersSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_queryset(self) -> QuerySet:
        group = self.get_group()
        lesson = self.get_lesson()
        queryset = LessonResult.objects.filter(student__group__name=group,
                                               lesson_number=lesson)
        user = self.request.user
        if user.is_superuser:
            return queryset
        return queryset.exclude(student__group__name=GROUP_ADMINS)

    def create(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def partial_update(self, request: Request, *args, **kwargs) -> Response:
        raise MethodNotAllowed(request.method)

    def get_group(self) -> str:
        group = self.kwargs['group']
        group_queryset = Group.objects.filter(name=group)
        if not group_queryset.exists():
            raise NotFound('Group not found.')
        return group

    def get_lesson(self) -> int:
        lesson = int(self.kwargs['lesson'])
        if not Lessons.lesson_exists(lesson):
            raise NotFound('Lesson not found.')
        return lesson
