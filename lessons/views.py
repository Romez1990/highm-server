from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from users.permissions import IsStudent
from users.utils import get_n
from .base import LessonTitleSerializer
from .lessons import Lessons


@api_view(['GET'])
@permission_classes([IsStudent])
def lesson_list(request: Request) -> Response:
    lessons = Lessons.get_lesson_list()
    serializer = LessonTitleSerializer(lessons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsStudent])
def lesson_retrieve(request: Request, lesson_pk: int) -> Response:
    n = get_n(request)
    lesson = Lessons.get_lesson(lesson_pk, n)
    if lesson is None:
        raise Http404()
    serializer = lesson.serializer(lesson)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsStudent])
def lesson_check(request, lesson_pk: int) -> Response:
    serializer_class_type = Lessons.get_lesson_results_serializer(lesson_pk)
    if serializer_class_type is None:
        raise Http404()
    serializer = serializer_class_type(data=request.data)
    serializer.is_valid(raise_exception=True)
    n = get_n(request)
    lesson_results = Lessons.get_lesson_results(lesson_pk, n,
                                                serializer.validated_data)
    check_results = lesson_results.check()
    return Response({
        'results': check_results
    })
