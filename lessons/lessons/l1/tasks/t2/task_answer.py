from rest_framework.fields import (
    IntegerField,
)

from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.base import TaskAnswerBase, TaskAnswerSerializerBase
from .task import Task


class TaskResultSerializer(TaskAnswerSerializerBase):
    product = MatrixField(child=IntegerField())
    trace = IntegerField()


class TaskAnswer(TaskAnswerBase):
    serializer = TaskResultSerializer
    task_type = Task

    def __init__(self, n: int, product: MatrixInt, trace: int) -> None:
        super().__init__(n)
        self.product = product
        self.trace = trace
