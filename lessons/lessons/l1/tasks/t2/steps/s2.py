from numpy import trace

from lessons.base import StepBase
from ..task_answer import TaskAnswer


class Step(StepBase):
    def check(self, task_answer: TaskAnswer) -> bool:
        return task_answer.trace == trace(task_answer.product)
