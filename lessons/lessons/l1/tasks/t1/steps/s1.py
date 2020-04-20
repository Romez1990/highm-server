from __future__ import annotations
from typing import TYPE_CHECKING

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..answer import Answer1


class Step1(StepBase):
    def check(self, answer: Answer1) -> bool:
        return answer.which_of_products == 'AB'
