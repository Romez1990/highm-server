from rest_framework.serializers import (
    IntegerField,
)

from lessons.base import TaskBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.serializers_for_student import TaskSerializerBase


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
