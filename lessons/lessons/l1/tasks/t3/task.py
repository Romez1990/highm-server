from rest_framework.fields import IntegerField

from lessons.base.task import TaskSerializerBase
from lessons.utils.serializer import MatrixField
from lessons.utils.math import MatrixInt
from lessons.base import TaskBase


class TaskSerializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())


class Task(TaskBase):
    serializer = TaskSerializer

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.matrix_a = self._get_matrix_a(self.n)

    def _get_text(self) -> str:
        return 'Вычислить определитель матрицы третьего порядка:'

    def _get_matrix_a(self, n: int) -> MatrixInt:
        return [
            [1, 2, n - 15],
            [n - 10, 0, 4],
            [2, 1, 7],
        ]
