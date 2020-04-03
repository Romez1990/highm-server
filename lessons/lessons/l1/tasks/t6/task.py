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
        return 'Вычислить определитель матрицы четвёртого порядка:'

    def _get_matrix_a(self, n: int) -> MatrixInt:
        return [
            [0, 1, 1, n - 10],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [n - 20, 1, 1, 0],
        ]
