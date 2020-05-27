from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from lessons.base.answer import AnswerBase


class StepBase:
    max_points: int

    def __init__(self, answer: AnswerBase) -> None:
        self.points = self.max_points if self._check(answer) else 0

    def _check(self, answer: AnswerBase) -> bool:
        raise NotImplementedError
