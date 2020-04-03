from rest_framework.fields import (
    IntegerField,
)

from lessons.base import TaskAnswerBase, TaskAnswerSerializerBase
from .task import Task


class TaskResultSerializer(TaskAnswerSerializerBase):
    determinant = IntegerField()


class TaskAnswer(TaskAnswerBase):
    serializer = TaskResultSerializer

    def __init__(self, n: int, determinant: int) -> None:
        super().__init__(n)
        self.task = Task(n)
        self.determinant = determinant
