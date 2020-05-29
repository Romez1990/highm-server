from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

from numpy import array, dot

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task1
    from ..answer import Answer1


class Step2(StepBase):
    max_points = 1

    _task: Task1
    _answer: Answer1

    def _check(self) -> bool:
        answered_product = self._answer.product

        matrix_a = self._task.matrix_a
        matrix_b = self._task.matrix_b

        a = array(matrix_a)
        b = array(matrix_b)
        product = dot(a, b).tolist()
        return answered_product == product
