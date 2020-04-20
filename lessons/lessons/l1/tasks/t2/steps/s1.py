from __future__ import annotations
from typing import TYPE_CHECKING
from numpy import array
from numpy.linalg import matrix_power

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..answer import Answer2


class Step1(StepBase):
    def check(self, answer: Answer2) -> bool:
        a = array(answer.task.matrix_a)
        product = matrix_power(a, 3)
        return answer.product == product.tolist()
