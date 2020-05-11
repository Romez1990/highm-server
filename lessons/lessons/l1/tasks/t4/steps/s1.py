from typing import (
    TYPE_CHECKING,
)
from numpy import array, identity
from numpy.linalg import matrix_power

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task4
    from ..answer import Answer4


class Step1(StepBase):
    max_points = 3

    _task: 'Task4'
    _answer: 'Answer4'

    def _check(self) -> bool:
        answered_result = self._answer.result

        matrix_a = self._task.matrix_a
        coefficient_a = self._task.coefficient_a
        coefficient_b = self._task.coefficient_b
        coefficient_c = self._task.coefficient_c

        x = array(matrix_a)
        assert x.shape[0] == x.shape[1], 'the matrix should be square'
        a_x_2 = coefficient_a * matrix_power(x, 2)
        b_x = coefficient_b * x
        c = coefficient_c * identity(x.shape[0])
        f_x = a_x_2 + b_x + c
        result = f_x.tolist()
        return answered_result == result
