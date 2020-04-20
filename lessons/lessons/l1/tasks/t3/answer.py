from rest_framework.fields import (
    IntegerField,
)

from lessons.base import AnswerBase, AnswerSerializerBase
from .task import Task3
from .steps.s1 import Step1


class Answer3Serializer(AnswerSerializerBase):
    determinant = IntegerField()


class Answer3(AnswerBase):
    _task_type = Task3
    task: Task3
    _steps = [
        Step1,
    ]

    def __init__(self, n: int, determinant: int) -> None:
        super().__init__(n)
        self.determinant = determinant
