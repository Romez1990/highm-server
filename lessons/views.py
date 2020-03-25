from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from users.permissions import IsStudent
from .serializers import LessonSerializer, LessonDetailsSerializer
from .load import lessons, get_lesson


@api_view(['GET'])
@permission_classes([IsStudent])
def lesson_list(request):
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsStudent])
def lesson_retrieve(request, lesson_pk):
    try:
        lesson = get_lesson(lesson_pk)
    except ValueError:
        raise Http404()
    serializer = LessonDetailsSerializer(lesson, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsStudent])
def lesson_check(request, lesson_pk):
    try:
        lesson = get_lesson(lesson_pk)
    except ValueError:
        raise Http404()
    return Response(
        [check_task(Task, request, index)
         for index, Task in enumerate(lesson.tasks)]
    )


def check_task(Task, request, index):
    result_serializer = Task.result_serializer(data=request.data[index],
                                               context={'request': request})
    if not result_serializer.is_valid():
        return result_serializer.errors
    task = Task(**result_serializer.data)
    return task.check()
