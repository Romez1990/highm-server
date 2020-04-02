from typing import List

from lessons.task_base import TaskBase
from .serializer import TaskGivenSerializer, TaskResultSerializer
from .given import get_matrix_a, get_matrix_b


class Task(TaskBase):
    given_serializer = TaskGivenSerializer
    result_serializer = TaskResultSerializer
    text = 'Найти то из произведений матриц <formula>AB</formula> и ' \
           '<formula>BA</formula>, которое существует:'

    def __init__(
        self,
        n: int,
        which_of_products: str,
        product: List[List[int]]
    ) -> None:
        self.n = n
        self.text = 'Найти то из произведений матриц <formula>AB</formula> и ' \
                    '<formula>BA</formula>, которое существует: '
        self.matrix_a = get_matrix_a(self.n)
        self.matrix_b = get_matrix_b(self.n)
        self.which_of_products = which_of_products
        self.product = product
