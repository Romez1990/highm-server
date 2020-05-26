from typing import List, Dict, Type
from rest_framework.serializers import (
    Serializer,
    CharField,
    BooleanField,
    ListField,
)

from users.models import Student
from ..models import LessonResult
from .task import TaskBase


class LessonBasicSerializerBase(Serializer):
    title = CharField(max_length=150)


class LessonBasicSerializer(LessonBasicSerializerBase):
    passed = BooleanField()


class LessonBaseSerializer(LessonBasicSerializerBase):
    goals = ListField(child=CharField(max_length=300))


class LessonBasicBaseBase:
    title: str


class LessonBasicBase(LessonBasicBaseBase):
    number: int
    passed: bool

    def __init__(self, student: Student = None) -> None:
        if student is None:
            return

        queryset = LessonResult.objects.filter(student=student,
                                               lesson_number=self.number)
        self.passed = queryset.exists()


class LessonBase(LessonBasicBaseBase):
    serializer: Type[LessonBaseSerializer]
    goals: List[str] = []
    tasks: Dict[str, TaskBase]

    def __init__(self, n: int) -> None:
        self.n = n
