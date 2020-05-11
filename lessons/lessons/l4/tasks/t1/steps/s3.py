from typing import (
    TYPE_CHECKING,
)
from numpy import array, sum, allclose

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task1
    from ..answer import Answer1


class Step3(StepBase):
    max_points = 1

    _task: 'Task1'
    _answer: 'Answer1'

    def _check(self) -> bool:
        answered_y = array([answer['y']
                            for answer in self._answer.intermediate_results])
        answered_result = self._answer.result

        a = self._task.a
        b = self._task.b
        N = self._task.N
        tolerance = self._task.tolerance

        answered_y[0] /= 2
        answered_y[-1] /= 2
        dx = (b - a) / N
        result = sum(answered_y) * dx
        atol = 10 ** -tolerance
        return allclose(answered_result, round(result, tolerance),
                        rtol=0, atol=atol)
