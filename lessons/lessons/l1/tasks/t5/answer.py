from rest_framework.fields import IntegerField

from lessons.base import AnswerBase, AnswerSerializerBase
from .task import Task


class TaskResultSerializer(AnswerSerializerBase):
    x1 = IntegerField()
    x2 = IntegerField()


class Answer(AnswerBase):
    serializer = TaskResultSerializer
    task_type = Task

    def __init__(self, n: int, x1: int, x2: int) -> None:
        super().__init__(n)
        self.x1 = x1
        self.x2 = x2
