from rest_framework.fields import IntegerField

from lessons.base import TaskBase, TaskSerializerBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField


class Task2Serializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())


class Task2(TaskBase):
    text = 'Найти матрицу <formula>A^3</formula> и её след:'

    @property
    def matrix_a(self) -> MatrixInt:
        n = self.n
        return [
            [1, -2],
            [n - 10, -4],
        ]
