from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response

from users.permissions import IsStudent
from .base import LessonBasicSerializer
from .lessons import Lessons


class LessonViewSet(ViewSet):
    permission_classes = [IsStudent]

    def list(self, request: Request) -> Response:
        lessons = Lessons.get_lesson_list()
        serializer = LessonBasicSerializer(lessons, many=True)
        return Response(serializer.data)
