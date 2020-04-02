from typing import List

from lessons.task_base import TaskBase
from .serializer import TaskGivenSerializer, TaskResultSerializer
from .given import get_matrix_a


class Task(TaskBase):
    given_serializer = TaskGivenSerializer
    result_serializer = TaskResultSerializer

    def __init__(self, n: int, determinant: int) -> None:
        self.n = n
        self.text = 'Вычислить определитель матрицы третьего порядка:'
        self.matrix_a = get_matrix_a(self.n)
        self.determinant = determinant
