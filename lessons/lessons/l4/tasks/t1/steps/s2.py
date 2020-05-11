from typing import (
    TYPE_CHECKING,
)
from numpy import array, ndarray, allclose, round

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task1
    from ..answer import Answer1


class Step2(StepBase):
    max_points = 1

    _task: 'Task1'
    _answer: 'Answer1'

    def _check(self) -> bool:
        answered_x = array([answer['x']
                            for answer in self._answer.intermediate_results])
        answered_y = array([answer['y']
                            for answer in self._answer.intermediate_results])

        f = self._task.f
        tolerance = self._task.tolerance

        y: ndarray = f(answered_x)
        atol = 10 ** -tolerance
        return allclose(answered_y, round(y, tolerance), rtol=0, atol=atol)
