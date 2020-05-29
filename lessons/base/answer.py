from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Type,
    List,
    Dict,
    Any,
)

if TYPE_CHECKING:
    from .task import TaskBase
    from .step import StepBase


class AnswerBase:
    _step_classes: List[Type[StepBase]]
    _task_class: Type[TaskBase]

    def __init__(self, n: int) -> None:
        self._n = n
        self._task = self._task_class(n)
        self._steps: List[StepBase] = []

    def check(self) -> None:
        task = self._task
        self._steps = [step(task, self) for step in self._step_classes]

    @property
    def points(self) -> int:
        if not self._steps:
            raise ValueError('Steps are empty')
        return sum(step.points for step in self._steps)

    @classmethod
    def max_points(cls) -> int:
        return sum(step.max_points for step in cls._step_classes)

    def to_json(self) -> Dict[str, Any]:
        raise NotImplementedError
