from rest_framework.fields import IntegerField

from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.base import TaskAnswerBase, TaskAnswerSerializerBase
from .task import Task


class TaskResultSerializer(TaskAnswerSerializerBase):
    result = MatrixField(child=IntegerField())


class TaskAnswer(TaskAnswerBase):
    serializer = TaskResultSerializer
    task_type = Task

    def __init__(self, n: int, result: MatrixInt) -> None:
        super().__init__(n)
        self.result = result
