from typing import (
    TYPE_CHECKING,
)
from numpy import array
from numpy.linalg import matrix_power

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task2
    from ..answer import Answer2


class Step1(StepBase):
    max_points = 1

    _task: 'Task2'
    _answer: 'Answer2'

    def _check(self) -> bool:
        answered_product = self._answer.product

        matrix_a = self._task.matrix_a

        a = array(matrix_a)
        product = matrix_power(a, 3).tolist()
        return answered_product == product
