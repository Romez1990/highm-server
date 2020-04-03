from numpy import array
from numpy.linalg import matrix_power

from lessons.base import StepBase
from ..task_answer import TaskAnswer


class Step(StepBase):
    def check(self, task_answer: TaskAnswer) -> bool:
        a = array(task_answer.task.matrix_a)
        product = matrix_power(a, 3)
        return task_answer.product == product.tolist()
