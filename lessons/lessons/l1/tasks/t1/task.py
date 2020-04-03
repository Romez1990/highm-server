from rest_framework.fields import IntegerField

from lessons.utils.math import MatrixInt
from lessons.base import TaskBase, TaskSerializerBase
from lessons.utils.serializer import MatrixField


class TaskSerializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())
    matrix_b = MatrixField(child=IntegerField())


class Task(TaskBase):
    serializer = TaskSerializer

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.matrix_a = self._get_matrix_a(n)
        self.matrix_b = self._get_matrix_b(n)

    def _get_text(self) -> str:
        return 'Найти то из произведений матриц <formula>AB</formula> и ' \
               '<formula>BA</formula>, которое существует: '

    def _get_matrix_a(self, n: int) -> MatrixInt:
        return [
            [1, n],
            [3, 4],
        ]

    def _get_matrix_b(self, n: int) -> MatrixInt:
        return [
            [n - 5, 1, 3],
            [0, 0, 1],
        ]
