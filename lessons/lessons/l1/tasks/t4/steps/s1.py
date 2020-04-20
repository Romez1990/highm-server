from __future__ import annotations
from typing import TYPE_CHECKING
from numpy import array, identity
from numpy.linalg import matrix_power

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..answer import Answer4


class Step1(StepBase):
    def check(self, answer: Answer4) -> bool:
        task = answer.task
        x = array(task.matrix_a)
        assert x.shape[0] == x.shape[1], 'the matrix should be square'
        a_x_2 = task.coefficient_a * matrix_power(x, 2)
        b_x = task.coefficient_b * x
        c = task.coefficient_c * identity(x.shape[0])
        f_x = a_x_2 + b_x + c
        return answer.result == f_x.tolist()
