from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lessons.base.task_answer import TaskAnswerBase


class StepBase:
    def check(self, task_answer: TaskAnswerBase) -> bool:
        raise NotImplementedError
