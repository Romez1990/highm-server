from rest_framework.fields import (
    IntegerField,
)

from lessons.base import AnswerBase, AnswerSerializerBase
from .task import Task6
from .steps.s1 import Step1


class Answer6Serializer(AnswerSerializerBase):
    determinant = IntegerField()


class Answer6(AnswerBase):
    _task_type = Task6
    task: Task6
    _steps = [
        Step1,
    ]

    def __init__(self, n: int, determinant: int) -> None:
        super().__init__(n)
        self.determinant = determinant
