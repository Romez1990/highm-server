from __future__ import annotations
from typing import TYPE_CHECKING
from lessons.base import StepBase

if TYPE_CHECKING:
    from ..answer import Answer5


class Step1(StepBase):
    def check(self, answer: Answer5) -> bool:
        return answer.x1 == 0 and answer.x2 == 1
