from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Union,
)

if TYPE_CHECKING:
    from lessons.base.answer import TaskBase, AnswerBase


class StepBase:
    max_points: int

    def __init__(self, task: TaskBase, answer: AnswerBase) -> None:
        self._task = task
        self._answer = answer
        result = self._check()
        self.points = self._process_result(result)

    def _check(self) -> Union[bool, int]:
        raise NotImplementedError

    def _process_result(self, result: Union[bool, int]) -> int:
        if type(result) == int:
            points = result
            if points < 0:
                raise ValueError('Result cannot be less than 0 points')
            if points > self._answer.max_points():
                raise ValueError('Result cannot be greater than max points')
            return points
        return self.max_points if result else 0
