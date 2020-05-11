from typing import (
    TYPE_CHECKING,
)
from numpy import round
from scipy.optimize import bisect

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task1
    from ..answer import Answer1


class Step1(StepBase):
    max_points = 3

    _task: 'Task1'
    _answer: 'Answer1'

    def _check(self) -> int:
        answered_x = self._answer.x

        f = self._task.equation
        a = self._task.a
        b = self._task.b
        epsilon = self._task.epsilon
        tolerance = self._task.tolerance

        x: float = bisect(f, a, b, xtol=epsilon)
        if round(x, tolerance) == round(answered_x, tolerance):
            return self.max_points
        if round(x, tolerance - 1) == round(answered_x, tolerance - 1):
            return self.max_points - 1
        if round(x, tolerance - 3) == round(answered_x, tolerance - 3):
            return self.max_points - 2
        return 0
