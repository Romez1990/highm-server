from numpy import array, identity
from numpy.linalg import matrix_power

from lessons.base import StepBase
from ..task_answer import TaskAnswer


class Step(StepBase):
    def check(self, task_answer: TaskAnswer) -> bool:
        task = task_answer.task
        x = array(task.matrix_a)
        assert x.shape[0] == x.shape[1], 'the matrix should be square'
        a_x_2 = task.coefficient_a * matrix_power(x, 2)
        b_x = task.coefficient_b * x
        c = task.coefficient_c * identity(x.shape[0])
        f_x = a_x_2 + b_x + c
        return task_answer.result == f_x.tolist()
