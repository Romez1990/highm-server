from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)
from numpy import allclose
from numpy.linalg import solve

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task1
    from ..answer import Answer1


class Step1(StepBase):
    max_points = 3

    _task: Task1
    _answer: Answer1

    def _check(self) -> bool:
        x = self._answer.x
        y = self._answer.y
        z = self._answer.z

        coefficient_matrix = self._task.coefficient_matrix
        constant_terms_vector = self._task.constant_terms_vector

        results = solve(coefficient_matrix, constant_terms_vector)
        return allclose([x, y, z], results)
