from rest_framework.fields import IntegerField

from lessons.utils.math import MatrixInt
from lessons.base import TaskBase, TaskSerializerBase
from lessons.utils.serializer import MatrixField


class TaskSerializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())
    matrix_b = MatrixField(child=IntegerField())


class Task(TaskBase):
    serializer = TaskSerializer

    text = 'Найти то из произведений матриц <formula>AB</formula> и ' \
           '<formula>BA</formula>, которое существует: '

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
