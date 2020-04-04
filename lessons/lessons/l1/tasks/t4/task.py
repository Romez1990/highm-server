from rest_framework.fields import IntegerField

from lessons.utils.serializer import MatrixField
from lessons.utils.math import number_to_expression
from lessons.base import TaskBase, TaskSerializerBase


class TaskSerializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())


class Task(TaskBase):
    serializer = TaskSerializer

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.coefficient_a = n - 8
        self.coefficient_b = n
        self.coefficient_c = -5

    @property
    def text(self) -> str:
        return 'Найти значение многочлена <formula>f(x)</formula> от матрицы ' \
               '<formula>A</formula>: ' \
               '<formula>f(x) = ' \
               f'{number_to_expression(self.coefficient_a, True)}x^2 ' \
               f'{number_to_expression(self.coefficient_b)}x ' \
               f'{number_to_expression(self.coefficient_c)}</formula>'

    matrix_a = [
        [5, 2, -3],
        [1, 3, -1],
        [2, 2, 1],
    ]
