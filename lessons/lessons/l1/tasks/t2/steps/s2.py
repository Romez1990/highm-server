from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)
from numpy import trace

from lessons.base import StepBase

if TYPE_CHECKING:
    from ..answer import Answer2


class Step2(StepBase):
    max_points = 1

    def _check(self, answer: Answer2) -> bool:
        return answer.trace == trace(answer.product)
