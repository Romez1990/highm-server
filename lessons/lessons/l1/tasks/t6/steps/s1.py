from numpy import array
from numpy.linalg import det

from lessons.base import StepBase
from ..task_answer import TaskAnswer


class Step(StepBase):
    def check(self, task_answer: TaskAnswer) -> bool:
        a = array(task_answer.task.matrix_a)
        determinant = det(a)
        return task_answer.determinant == int(round(determinant))
