from numpy import allclose
from numpy.linalg import solve

from lessons.base import StepBase
from ..task_answer import TaskAnswer


class Step(StepBase):
    def check(self, task_answer: TaskAnswer) -> bool:
        results = solve(task_answer.task.coefficient_matrix,
                        task_answer.task.constant_terms_vector)
        return allclose([task_answer.x, task_answer.y, task_answer.z], results)
