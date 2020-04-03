from __future__ import annotations
from typing import TYPE_CHECKING, Type, List
from rest_framework.serializers import Serializer

from lessons.utils.serializer import StudentNField

if TYPE_CHECKING:
    from .task import TaskBase
    from .step import StepBase


class TaskAnswerSerializerBase(Serializer):
    n = StudentNField()


class TaskAnswerBase:
    serializer: Type[TaskAnswerSerializerBase]
    steps: List[StepBase] = []

    def __init__(self, n: int) -> None:
        self.n = n
        self.task: TaskBase

    def check(self) -> bool:
        return all(map(lambda step: step.check(self), self.steps))
