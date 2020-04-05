from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lessons.base.answer import AnswerBase


class StepBase:
    def check(self, answer: AnswerBase) -> bool:
        raise NotImplementedError
