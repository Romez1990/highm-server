from typing import (
    Dict,
    Any,
)
from rest_framework.serializers import (
    IntegerField,
)

from lessons.base import AnswerBase
from lessons.serializers_for_student import AnswerSerializerBase
from .task import Task3
from .steps.s1 import Step1


class Answer3Serializer(AnswerSerializerBase):
    determinant = IntegerField()


class Answer3(AnswerBase):
    _task_class = Task3
    _task: Task3
    _step_classes = [
        Step1,
    ]

    def __init__(self, n: int, determinant: int) -> None:
        super().__init__(n)
        self.determinant = determinant

    def to_json(self) -> Dict[str, Any]:
        return {
            'determinant': self.determinant,
        }
