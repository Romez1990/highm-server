from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..task import Task1
    from ..answer import Answer1


class Step1(StepBase):
    max_points = 1

    _task: Task1
    _answer: Answer1

    def _check(self) -> bool:
        which_of_products = self._answer.which_of_products
        return which_of_products == 'AB'
