from __future__ import annotations
from math import fabs, cos
from typing import (
    TYPE_CHECKING,
)
from scipy.optimize import bisect

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task1
    from ..answer import Answer1


class Step1(StepBase):
    max_points = 1

    _task: Task1
    _answer: Answer1

    def _check(self) -> bool:
        answered_x = self._answer.x

        coefficient = self._task.coefficient
        a = self._task.a
        b = self._task.b
        epsilon = self._task.epsilon

        f = self._f
        x: float = bisect(f, a, b, args=(coefficient,))
        accuracy = fabs(x - answered_x)
        return accuracy <= epsilon

    def _f(self, x: float, coefficient: float) -> float:
        return coefficient * cos(x) - x ** 2
