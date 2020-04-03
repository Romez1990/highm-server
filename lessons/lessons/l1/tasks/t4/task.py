from rest_framework.fields import IntegerField

from lessons.utils.serializer import MatrixField
from lessons.utils.math import MatrixInt, number_to_expression
from lessons.base import TaskBase, TaskSerializerBase


class TaskSerializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())


class Task(TaskBase):
    serializer = TaskSerializer

    def __init__(self, n: int) -> None:
        self.coefficient_a = n - 8
        self.coefficient_b = n
        self.coefficient_c = -5
        super().__init__(n)
        self.matrix_a = self._get_matrix_a(self.n)

    def _get_text(self) -> str:
        return 'Найти значение многочлена <formula>f(x)</formula> от матрицы ' \
               '<formula>A</formula>: ' \
               '<formula>f(x) = ' \
               f'{number_to_expression(self.coefficient_a, True)}x^2 ' \
               f'{number_to_expression(self.coefficient_b)}x ' \
               f'{number_to_expression(self.coefficient_c)}</formula>'

    def _get_matrix_a(self, _: int) -> MatrixInt:
        return [
            [5, 2, -3],
            [1, 3, -1],
            [2, 2, 1],
        ]
