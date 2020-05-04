from typing import List, Dict, Type
from rest_framework.serializers import (
    Serializer,
    CharField,
    ListField,
)

from .task import TaskBase


class LessonBasicSerializer(Serializer):
    title = CharField(max_length=150)


class LessonBaseSerializer(Serializer):
    title = CharField(max_length=150)
    goals = ListField(child=CharField(max_length=300))


class LessonBase:
    serializer: Type[LessonBaseSerializer]
    title: str
    goals: List[str] = []
    tasks: Dict[str, TaskBase]

    def __init__(self, n: int) -> None:
        self.n = n
