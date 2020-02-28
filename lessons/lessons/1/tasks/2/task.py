from typing import List

from lessons.task_base import TaskBase
from .serializer import TaskGivenSerializer, TaskResultSerializer
from .given import get_matrix_a


class Task(TaskBase):
    given_serializer = TaskGivenSerializer
    result_serializer = TaskResultSerializer
    text = 'Найти матрицу <formula>A^3</formula> и её след:'

    def __init__(self, n: int, product: List[List[int]]) -> None:
        self.n = n
        self.matrix_a = get_matrix_a(self.n)
        self.product = product


# answer = {
#     "which_of_products": "AB",
#     "product": [
#         [-4, 1, 4],
#         [-12, 3, 13]
#     ]
# }
