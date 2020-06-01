from typing import List
from rest_framework.serializers import (
    IntegerField,
    ListField,
)

from lessons.base import TaskBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.serializers_for_student import TaskSerializerBase


class Task2Serializer(TaskSerializerBase):
    coefficient_matrix = MatrixField(child=IntegerField())
    constant_terms_vector = ListField(child=IntegerField())


class Task2(TaskBase):
    text = 'Решить (любым методом) систему уравнений, заданную в виде ' \
           '<formula>A * X = B</formula>, где <formula>A</formula> – матрица ' \
           'системы, <formula>B</formula> – столбец свободных элементов:'

    @property
    def coefficient_matrix(self) -> MatrixInt:
        index = (self.n - 1) % len(self.coefficient_matrix_variants)
        return self.coefficient_matrix_variants[index]

    @property
    def constant_terms_vector(self) -> List[int]:
        index = (self.n - 1) % len(self.constant_terms_vector_variants)
        return self.constant_terms_vector_variants[index]

    coefficient_matrix_variants: List[MatrixInt] = [
        [
            [3, 2, -2],
            [1, 1, 1],
            [2, -3, -3],
        ],
        [
            [2, 1, 1],
            [1, 2, 1],
            [1, 1, 2],
        ],
    ]

    constant_terms_vector_variants: List[List[int]] = [
        [-2, 0, 10],
        [3, 0, 9],
    ]
