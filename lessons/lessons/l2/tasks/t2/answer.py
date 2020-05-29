from typing import (
    Dict,
    Any,
)
from rest_framework.fields import (
    IntegerField,
)

from lessons.base import AnswerBase
from lessons.serializers_for_student import AnswerSerializerBase
from .task import Task2
from .steps.s1 import Step1


class Answer2Serializer(AnswerSerializerBase):
    x = IntegerField()
    y = IntegerField()
    z = IntegerField()


class Answer2(AnswerBase):
    _task_class = Task2
    _step_classes = [
        Step1,
    ]

    def __init__(
            self,
            n: int,
            x: int,
            y: int,
            z: int,
    ) -> None:
        super().__init__(n)
        self.x = x
        self.y = y
        self.z = z

    def to_json(self) -> Dict[str, Any]:
        return {
            'x': self.x,
            'y': self.y,
            'z': self.z,
        }
