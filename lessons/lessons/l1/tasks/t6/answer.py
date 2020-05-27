from typing import (
    Dict,
    Any,
)
from rest_framework.fields import (
    IntegerField,
)

from lessons.base import AnswerBase
from lessons.serializers_for_student import AnswerSerializerBase
from .task import Task6
from .steps.s1 import Step1


class Answer6Serializer(AnswerSerializerBase):
    determinant = IntegerField()


class Answer6(AnswerBase):
    _task_type = Task6
    _task: Task6
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
