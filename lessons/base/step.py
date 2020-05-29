from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from lessons.base.answer import TaskBase, AnswerBase


class StepBase:
    max_points: int

    def __init__(self, task: TaskBase, answer: AnswerBase) -> None:
        self._task = task
        self._answer = answer
        self.points = self.max_points if self._check() else 0

    def _check(self) -> bool:
        raise NotImplementedError
