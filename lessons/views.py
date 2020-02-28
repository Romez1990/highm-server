from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from users.permissions import IsStudent
from .serializers import LessonSerializer, LessonDetailsSerializer
from .load import lessons, get_lesson, get_task


@api_view(['GET'])
@permission_classes([IsStudent])
def lesson_list(request):
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsStudent])
def lesson_retrieve(request, lesson_pk):
    lesson = get_lesson(lesson_pk)
    serializer = LessonDetailsSerializer(lesson, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsStudent])
def lesson_check(request, lesson_pk):
    return Response('not implemented')


@api_view(['POST'])
@permission_classes([IsStudent])
def task_check(request, lesson_pk, task_pk):
    try:
        lesson = get_lesson(lesson_pk)
        Task = get_task(lesson, task_pk)
    except ValueError:
        raise Http404()
    given_serializer = Task.given_serializer(data=request.data,
                                             context={'request': request})
    given_serializer.is_valid(raise_exception=True)
    task = Task(**given_serializer.data)
    result = task.check()
    if type(result) == int:
        return Response({'error_step': result})
    if type(result) == bool:
        return Response({'success': result})
    raise TypeError(f'result cannot be {type(result)}')
