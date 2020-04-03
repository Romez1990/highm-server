from numpy import array, dot

from lessons.base import StepBase
from ..task_answer import TaskAnswer


class Step(StepBase):
    def check(self, task_answer: TaskAnswer) -> bool:
        a = array(task_answer.task.matrix_a)
        b = array(task_answer.task.matrix_b)
        product = dot(a, b)
        return task_answer.product == product.tolist()
