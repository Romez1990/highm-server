from rest_framework.fields import (
    IntegerField,
)

from lessons.base import AnswerBase, AnswerSerializerBase
from .task import Task2
from .steps.s1 import Step1


class Answer2Serializer(AnswerSerializerBase):
    x = IntegerField()
    y = IntegerField()
    z = IntegerField()


class Answer2(AnswerBase):
    _task_type = Task2
    task: Task2
    _steps = [
        Step1,
    ]

    def __init__(
        self,
        n: int,
        x: int,
        y: int,
        z: int,
    ) -> None:
        super().__init__(n)
        self.x = x
        self.y = y
        self.z = z
