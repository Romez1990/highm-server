from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)
from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task5
    from ..answer import Answer5


class Step1(StepBase):
    max_points = 2

    _task: Task5
    _answer: Answer5

    def _check(self) -> bool:
        x1 = self._answer.x1
        x2 = self._answer.x2

        return x1 == 0 and x2 == 1
