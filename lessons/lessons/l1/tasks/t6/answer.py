from rest_framework.fields import (
    IntegerField,
)

from lessons.base import AnswerBase, AnswerSerializerBase
from .task import Task


class TaskResultSerializer(AnswerSerializerBase):
    determinant = IntegerField()


class Answer(AnswerBase):
    serializer = TaskResultSerializer
    task_type = Task

    def __init__(self, n: int, determinant: int) -> None:
        super().__init__(n)
        self.determinant = determinant
