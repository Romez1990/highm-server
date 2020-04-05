from lessons.base import StepBase
from ..answer import Answer


class Step(StepBase):
    def check(self, answer: Answer) -> bool:
        return answer.x1 == 0 and answer.x2 == 1
