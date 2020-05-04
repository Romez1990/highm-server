from rest_framework.fields import IntegerField

from lessons.base import TaskBase, TaskSerializerBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField


class Task3Serializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())


class Task3(TaskBase):
    text = 'Вычислить определитель матрицы третьего порядка:'

    @property
    def matrix_a(self) -> MatrixInt:
        n = self.n
        return [
            [1, 2, n - 15],
            [n - 10, 0, 4],
            [2, 1, 7],
        ]
