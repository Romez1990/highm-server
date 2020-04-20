from __future__ import annotations
from typing import TYPE_CHECKING
from numpy import array
from numpy.linalg import det

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..answer import Answer3


class Step1(StepBase):
    def check(self, answer: Answer3) -> bool:
        a = array(answer.task.matrix_a)
        determinant = det(a)
        return answer.determinant == int(round(determinant))
