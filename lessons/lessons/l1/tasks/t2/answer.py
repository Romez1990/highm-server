from typing import (
    Dict,
    Any,
)
from rest_framework.fields import (
    IntegerField,
)

from lessons.base import AnswerBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.serializers_for_student import AnswerSerializerBase
from .task import Task2
from .steps.s1 import Step1
from .steps.s2 import Step2


class Answer2Serializer(AnswerSerializerBase):
    product = MatrixField(child=IntegerField())
    trace = IntegerField()


class Answer2(AnswerBase):
    _task_class = Task2
    _task: Task2
    _step_classes = [
        Step1,
        Step2,
    ]

    def __init__(self, n: int, product: MatrixInt, trace: int) -> None:
        super().__init__(n)
        self.product = product
        self.trace = trace

    def to_json(self) -> Dict[str, Any]:
        return {
            'product': self.product,
            'trace': self.trace,
        }
