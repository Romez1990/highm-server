from typing import (
    List,
    Dict,
)

from users.models import Student
from lessons.models import LessonResult
from .task import TaskBase


class LessonBaseBase:
    title: str


class LessonBasicBase(LessonBaseBase):
    passed: bool

    def __init__(self, number: int, student: Student) -> None:
        queryset = LessonResult.objects.filter(student=student,
                                               lesson_number=number)
        self.passed = queryset.exists()


class LessonBase(LessonBaseBase):
    goals: List[str]
    tasks: Dict[str, TaskBase]

    def __init__(self, n: int) -> None:
        self.n = n
