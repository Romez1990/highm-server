from typing import List
from rest_framework.fields import (
    IntegerField,
)

from lessons.base import TaskAnswerBase, TaskAnswerSerializerBase
from .task import Task


class TaskResultSerializer(TaskAnswerSerializerBase):
    x = IntegerField()
    y = IntegerField()
    z = IntegerField()


class TaskAnswer(TaskAnswerBase):
    serializer = TaskResultSerializer
    task_type = Task
    task: Task

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
