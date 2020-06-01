from rest_framework.serializers import (
    IntegerField,
)

from lessons.base import TaskBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.serializers_for_student import TaskSerializerBase


class Task1Serializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())
    matrix_b = MatrixField(child=IntegerField())


class Task1(TaskBase):
    text = 'Найти то из произведений матриц <formula>AB</formula> или ' \
           '<formula>BA</formula>, которое существует:'

    @property
    def matrix_a(self) -> MatrixInt:
        n = self.n
        return [
            [1, n],
            [3, 4],
        ]

    @property
    def matrix_b(self) -> MatrixInt:
        n = self.n
        return [
            [n - 5, 1, 3],
            [0, 0, 1],
        ]
