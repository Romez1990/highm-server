from numpy import array
from numpy.linalg import det

from lessons.base import StepBase
from ..answer import Answer


class Step(StepBase):
    def check(self, answer: Answer) -> bool:
        a = array(answer.task.matrix_a)
        determinant = det(a)
        return answer.determinant == int(round(determinant))
