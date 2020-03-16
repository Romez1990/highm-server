from typing import List

from lessons.task_base import TaskBase
from .serializer import TaskGivenSerializer, TaskResultSerializer
from .given import get_matrix_a


class Task(TaskBase):
    given_serializer = TaskGivenSerializer
    result_serializer = TaskResultSerializer
    text = 'Найти матрицу <formula>A^3</formula> и её след:'

    def __init__(self, n: int, product: List[List[int]], trace: int) -> None:
        self.n = n
        self.matrix_a = get_matrix_a(self.n)
        self.product = product
        self.trace = trace


answer = {
    "product": [
        [-4, 1],
        [-12, 3]
    ],
    "trace": "20",
}
