from rest_framework.fields import IntegerField

from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.base import AnswerBase, AnswerSerializerBase
from .task import Task


class TaskResultSerializer(AnswerSerializerBase):
    result = MatrixField(child=IntegerField())


class Answer(AnswerBase):
    serializer = TaskResultSerializer
    task_type = Task

    def __init__(self, n: int, result: MatrixInt) -> None:
        super().__init__(n)
        self.result = result
