from numpy import trace

from lessons.base import StepBase
from ..answer import Answer


class Step(StepBase):
    def check(self, answer: Answer) -> bool:
        return answer.trace == trace(answer.product)
