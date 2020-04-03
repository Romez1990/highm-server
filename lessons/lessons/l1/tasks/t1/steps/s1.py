from lessons.base import StepBase
from ..task_answer import TaskAnswer


class Step(StepBase):
    def check(self, task_answer: TaskAnswer) -> bool:
        return task_answer.which_of_products == 'AB'
