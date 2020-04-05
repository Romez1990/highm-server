from numpy import allclose
from numpy.linalg import solve

from lessons.base import StepBase
from ..answer import Answer


class Step(StepBase):
    def check(self, answer: Answer) -> bool:
        results = solve(answer.task.coefficient_matrix,
                        answer.task.constant_terms_vector)
        return allclose([answer.x, answer.y, answer.z], results)
