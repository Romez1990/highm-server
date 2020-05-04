from rest_framework.fields import (
    IntegerField,
)

from lessons.base import AnswerBase, AnswerSerializerBase
from .task import Task1
from .steps.s1 import Step1


class Answer1Serializer(AnswerSerializerBase):
    x = IntegerField()
    y = IntegerField()
    z = IntegerField()


class Answer1(AnswerBase):
    _task_type = Task1
    task: Task1
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
