from typing import (
    TYPE_CHECKING,
)
from numpy import array, ndarray, linspace, allclose

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task1
    from ..answer import Answer1


class Step1(StepBase):
    max_points = 1

    _task: 'Task1'
    _answer: 'Answer1'

    def _check(self) -> bool:
        answered_x = array([answer['x']
                            for answer in self._answer.intermediate_results])

        a = self._task.a
        b = self._task.b
        N = self._task.N

        x: ndarray = linspace(a, b, N + 1)
        return allclose(answered_x, x)
