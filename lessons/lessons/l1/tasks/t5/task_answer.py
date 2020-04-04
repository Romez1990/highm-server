from rest_framework.fields import IntegerField

from lessons.base import TaskAnswerBase, TaskAnswerSerializerBase
from .task import Task


class TaskResultSerializer(TaskAnswerSerializerBase):
    x1 = IntegerField()
    x2 = IntegerField()


class TaskAnswer(TaskAnswerBase):
    serializer = TaskResultSerializer
    task_type = Task

    def __init__(self, n: int, x1: int, x2: int) -> None:
        super().__init__(n)
        self.x1 = x1
        self.x2 = x2
