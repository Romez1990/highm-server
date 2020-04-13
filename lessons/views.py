from typing import Type
from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from users.permissions import IsStudent
from .base import AnswerBase
from .serializers import LessonSerializer, LessonDetailsSerializer
from .load import get_lessons, get_lesson


@api_view(['GET'])
@permission_classes([IsStudent])
def lesson_list(request: Request) -> Response:
    serializer = LessonSerializer(get_lessons(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsStudent])
def lesson_retrieve(request: Request, lesson_pk: int) -> Response:
    lesson = get_lesson(lesson_pk)
    if lesson is None:
        raise Http404()
    serializer = LessonDetailsSerializer(lesson, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsStudent])
def lesson_check(request, lesson_pk: int) -> Response:
    lesson = get_lesson(lesson_pk)
    if lesson is None:
        raise Http404()
    return Response(
        [check_task(Answer, request, index)
         for index, Answer in enumerate(lesson.answers)]
    )


def check_task(
    answer_type: Type[AnswerBase],
    request: Request,
    index: int,
) -> bool:
    serializer = answer_type.serializer(data=request.data['answers'][index],
                                             context={'request': request})
    if not serializer.is_valid():
        return serializer.errors
    answer = answer_type(**serializer.data)
    return answer.check()
