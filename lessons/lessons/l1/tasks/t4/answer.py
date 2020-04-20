from rest_framework.fields import IntegerField

from lessons.base import AnswerBase, AnswerSerializerBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from .task import Task4
from .steps.s1 import Step1


class Answer4Serializer(AnswerSerializerBase):
    result = MatrixField(child=IntegerField())


class Answer4(AnswerBase):
    _task_type = Task4
    task: Task4
    _steps = [
        Step1,
    ]

    def __init__(self, n: int, result: MatrixInt) -> None:
        super().__init__(n)
        self.result = result
