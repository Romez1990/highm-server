from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)
from numpy import array, dot

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..answer import Answer1


class Step2(StepBase):
    max_points = 1

    def _check(self, answer: Answer1) -> bool:
        a = array(answer.task.matrix_a)
        b = array(answer.task.matrix_b)
        product = dot(a, b)
        return answer.product == product.tolist()
