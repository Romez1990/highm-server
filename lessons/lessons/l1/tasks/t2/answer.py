from rest_framework.fields import (
    IntegerField,
)

from lessons.base import AnswerBase, AnswerSerializerBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from .task import Task2
from .steps.s1 import Step1
from .steps.s2 import Step2


class Answer2Serializer(AnswerSerializerBase):
    product = MatrixField(child=IntegerField())
    trace = IntegerField()


class Answer2(AnswerBase):
    _task_type = Task2
    task: Task2
    _steps = [
        Step1,
        Step2,
    ]

    def __init__(self, n: int, product: MatrixInt, trace: int) -> None:
        super().__init__(n)
        self.product = product
        self.trace = trace
