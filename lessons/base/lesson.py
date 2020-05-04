from typing import List
from rest_framework.serializers import (
    Serializer,
    CharField,
)


class LessonBasicSerializer(Serializer):
    title = CharField(max_length=150)


class LessonBase:
    title: str
    goals: List[str] = []
