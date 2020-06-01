from typing import (
    Dict,
    Any,
)
from rest_framework.serializers import (
    IntegerField,
)

from lessons.base import AnswerBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.serializers_for_student import AnswerSerializerBase
from .task import Task4
from .steps.s1 import Step1


class Answer4Serializer(AnswerSerializerBase):
    result = MatrixField(child=IntegerField())


class Answer4(AnswerBase):
    _task_class = Task4
    _task: Task4
    _step_classes = [
        Step1,
    ]

    def __init__(self, n: int, result: MatrixInt) -> None:
        super().__init__(n)
        self.result = result

    def to_json(self) -> Dict[str, Any]:
        return {
            'result': self.result,
        }
