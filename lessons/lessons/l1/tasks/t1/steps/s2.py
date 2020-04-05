from numpy import array, dot

from lessons.base import StepBase
from ..answer import Answer


class Step(StepBase):
    def check(self, answer: Answer) -> bool:
        a = array(answer.task.matrix_a)
        b = array(answer.task.matrix_b)
        product = dot(a, b)
        return answer.product == product.tolist()
