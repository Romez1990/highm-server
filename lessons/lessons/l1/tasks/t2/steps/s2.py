from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)
from numpy import trace

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task2
    from ..answer import Answer2


class Step2(StepBase):
    max_points = 1

    _task: Task2
    _answer: Answer2

    def _check(self) -> bool:
        answered_trace = self._answer.trace
        product = self._answer.product

        correct_trace = trace(product)
        return answered_trace == correct_trace
