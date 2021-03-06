from typing import List
from rest_framework.serializers import (
    IntegerField,
    ListField,
)

from lessons.base import TaskBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.serializers_for_student import TaskSerializerBase


class Task1Serializer(TaskSerializerBase):
    coefficient_matrix = MatrixField(child=IntegerField())
    constant_terms_vector = ListField(child=IntegerField())


class Task1(TaskBase):
    text = 'Методом обратной матрицы, по формулам Крамера и методом Гаусса ' \
           'решить систему уравнений:'

    @property
    def coefficient_matrix(self) -> MatrixInt:
        index = (self.n - 1) % len(self.coefficient_matrix_variants)
        return self.coefficient_matrix_variants[index]

    @property
    def constant_terms_vector(self) -> List[int]:
        index = (self.n - 1) % len(self.constant_terms_vector_variants)
        return self.constant_terms_vector_variants[index]

    coefficient_matrix_variants: List[MatrixInt] = [
        # 1
        [
            [2, -2, -1],
            [1, 2, 4],
            [3, -2, 1],
        ],
        # 2
        [
            [1, -2, -1],
            [1, 3, 2],
            [3, 1, 2],
        ],
        # 3
        [
            [-2, 2, -1],
            [1, -2, 1],
            [0, 3, -3],
        ],
        # 4
        [
            [2, 1, 1],
            [2, -2, 2],
            [2, 3, 0],
        ],
        # 5
        [
            [1, 2, -2],
            [-3, -2, 4],
            [2, 0, -2],
        ],
        # 6
        [
            [3, -4, -1],
            [1, -2, 1],
            [2, -3, -2],
        ],
        # 7
        [
            [1, 1, -1],
            [4, 2, 2],
            [3, 0, 1],
        ],
        # 8
        [
            [4, 3, -1],
            [2, -2, 1],
            [-1, 0, 1],
        ],
        # 9
        [
            [5, 1, -1],
            [-1, -2, 0],
            [3, -2, 0],
        ],
        # 10
        [
            [2, 1, -1],
            [1, 2, 2],
            [0, 2, 4],
        ],
        # 11
        [
            [2, 1, -1],
            [7, 3, 2],
            [1, 0, 4],
        ],
        # 12
        [
            [-2, -1, 1],
            [4, 2, -3],
            [1, 1, 0],
        ],
        # 13
        [
            [1, 1, 0],
            [-2, 8, 1],
            [3, 1, -1],
        ],
        # 14
        [
            [5, -2, 1],
            [0, 2, 2],
            [1, -1, -1],
        ],
        # 15
        [
            [1, 2, 1],
            [2, -2, 0],
            [-3, 1, -1],
        ],
        # 16
        [
            [0, 3, 4],
            [2, -2, 0],
            [-3, 1, -1],
        ],
        # 17
        [
            [7, 0, 3],
            [2, -2, 2],
            [1, -1, 2],
        ],
        # 18
        [
            [2, 3, 0],
            [2, 7, 1],
            [4, -1, 2],
        ],
        # 19
        [
            [4, -2, 1],
            [2, 0, -1],
            [-3, -1, 2],
        ],
        # 20
        [
            [2, -1, 2],
            [-2, 4, 3],
            [1, 0, 1],
        ],
        # 21
        [
            [2, 0, 1],
            [-2, -3, -1],
            [2, 2, 2],
        ],
        # 22
        [
            [1, 1, 0],
            [-2, -3, -2],
            [-3, -1, 1],
        ],
        # 23
        [
            [3, -4, -1],
            [1, -2, 1],
            [2, -3, -2],
        ],
        # 24
        [
            [1, 0, -2],
            [1, -2, 1],
            [-3, 5, 3],
        ],
        # 25
        [
            [4, 3, 0],
            [1, 2, 2],
            [-1, 2, 4],
        ],
        # 26
        [
            [0, 3, 1],
            [2, -2, -3],
            [-1, 1, 2],
        ],
        # 27
        [
            [2, 1, -1],
            [3, 4, 0],
            [3, 2, -1],
        ],
        # 28
        [
            [3, 1, -1],
            [0, -1, 4],
            [-1, -2, -3],
        ],
        # 29
        [
            [1, -2, 1],
            [4, 0, 2],
            [3, -1, 1],
        ],
        # 30
        [
            [-1, 2, -1],
            [2, 1, 1],
            [1, -3, 0],
        ],
        # 31
        [
            [2, 1, 1],
            [1, -2, 2],
            [2, 2, 0],
        ],
        # 32
        [
            [1, 0, -1],
            [2, -2, -2],
            [-3, -1, 1],
        ],
    ]

    constant_terms_vector_variants: List[List[int]] = [
        # 1
        [1, 2, 3],
        # 2
        [2, 2, 2],
        # 3
        [1, 2, 0],
        # 4
        [-2, 4, -2],
        # 5
        [1, 1, 2],
        # 6
        [2, 2, 2],
        # 7
        [2, 2, 2],
        # 8
        [8, 1, 4],
        # 9
        [-1, -2, 5],
        # 10
        [3, -1, 4],
        # 11
        [2, 1, -1],
        # 12
        [5, 4, 1],
        # 13
        [4, 4, 8],
        # 14
        [12, 0, -6],
        # 15
        [4, -4, 4],
        # 16
        [-20, -10, 30],
        # 17
        [14, 2, 1],
        # 18
        [10, -10, -20],
        # 19
        [2, 2, 6],
        # 20
        [5, 10, 5],
        # 21
        [2, 4, 6],
        # 22
        [4, 4, -3],
        # 23
        [-1, -1, 1],
        # 24
        [3, 3, 0],
        # 25
        [5, 2, 4],
        # 26
        [3, 2, -1],
        # 27
        [-2, 4, 3],
        # 28
        [-2, -1, -1],
        # 29
        [-2, 0, 2],
        # 30
        [-1, 2, 1],
        # 31
        [4, 4, 4],
        # 32
        [-1, 4, 2],
    ]
