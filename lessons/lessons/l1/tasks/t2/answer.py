from rest_framework.fields import (
    IntegerField,
)

from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.base import AnswerBase, AnswerSerializerBase
from .task import Task


class TaskResultSerializer(AnswerSerializerBase):
    product = MatrixField(child=IntegerField())
    trace = IntegerField()


class Answer(AnswerBase):
    serializer = TaskResultSerializer
    task_type = Task

    def __init__(self, n: int, product: MatrixInt, trace: int) -> None:
        super().__init__(n)
        self.product = product
        self.trace = trace
