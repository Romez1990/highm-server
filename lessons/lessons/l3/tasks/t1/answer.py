from typing import (
    Dict,
    Any,
)
from rest_framework.fields import (
    FloatField,
)

from lessons.base import AnswerBase
from lessons.serializers_for_student import AnswerSerializerBase
from .task import Task1
from .steps.s1 import Step1


class Answer1Serializer(AnswerSerializerBase):
    x = FloatField()


class Answer1(AnswerBase):
    _task_class = Task1
    _step_classes = [
        Step1,
    ]

    def __init__(
            self,
            n: int,
            x: float,
    ) -> None:
        super().__init__(n)
        self.x = x

    def to_json(self) -> Dict[str, Any]:
        return {
            'x': self.x,
        }
