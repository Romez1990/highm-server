from rest_framework.fields import IntegerField

from lessons.base.task import TaskSerializerBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.base import TaskBase


class Task6Serializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())


class Task6(TaskBase):
    text = 'Вычислить определитель матрицы четвёртого порядка:'

    @property
    def matrix_a(self) -> MatrixInt:
        n = self.n
        return [
            [0, 1, 1, n - 10],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [n - 20, 1, 1, 0],
        ]