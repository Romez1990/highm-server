from __future__ import annotations
from typing import TYPE_CHECKING
from numpy import allclose
from numpy.linalg import solve

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..answer import Answer1


class Step1(StepBase):
    def check(self, answer: Answer1) -> bool:
        results = solve(answer.task.coefficient_matrix,
                        answer.task.constant_terms_vector)
        return allclose([answer.x, answer.y, answer.z], results)
