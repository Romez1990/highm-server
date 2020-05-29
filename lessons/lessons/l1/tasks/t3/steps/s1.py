from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)
from numpy import array
from numpy.linalg import det

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task3
    from ..answer import Answer3


class Step1(StepBase):
    max_points = 1

    _task: Task3
    _answer: Answer3

    def _check(self) -> bool:
        answered_determinant = self._answer.determinant

        matrix_a = self._task.matrix_a

        a = array(matrix_a)
        determinant = round(det(a))
        return answered_determinant == determinant
