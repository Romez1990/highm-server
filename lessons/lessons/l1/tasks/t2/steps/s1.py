from numpy import array
from numpy.linalg import matrix_power

from lessons.base import StepBase
from ..answer import Answer


class Step(StepBase):
    def check(self, answer: Answer) -> bool:
        a = array(answer.task.matrix_a)
        product = matrix_power(a, 3)
        return answer.product == product.tolist()
