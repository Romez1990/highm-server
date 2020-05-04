from __future__ import annotations
from typing import TYPE_CHECKING, Type, List
from rest_framework.serializers import Serializer

if TYPE_CHECKING:
    from .task import TaskBase
    from .step import StepBase


class AnswerSerializerBase(Serializer):
    pass


class AnswerBase:
    _steps: List[Type[StepBase]] = []
    _task_type: Type[TaskBase]

    def __init__(self, n: int) -> None:
        self.n = n
        self.task = self._task_type(n)

    def check(self) -> bool:
        if not self._steps:
            raise ValueError(f'steps are empty at {self.__class__.__name__}')
        return all(map(lambda step: self._step_check(step), self._steps))

    def _step_check(self, step_type: Type[StepBase]) -> bool:
        step = step_type()
        return step.check(self)
