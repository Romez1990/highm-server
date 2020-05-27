from typing import (
    Dict,
    Any,
)
from rest_framework.fields import IntegerField

from lessons.base import AnswerBase
from lessons.serializers_for_student import AnswerSerializerBase
from .task import Task5
from .steps.s1 import Step1


class Answer5Serializer(AnswerSerializerBase):
    x1 = IntegerField()
    x2 = IntegerField()


class Answer5(AnswerBase):
    _task_type = Task5
    _task: Task5
    _step_classes = [
        Step1,
    ]

    def __init__(self, n: int, x1: int, x2: int) -> None:
        super().__init__(n)
        self.x1 = x1
        self.x2 = x2

    def to_json(self) -> Dict[str, Any]:
        return {
            'x1': self.x1,
            'x2': self.x2,
        }
