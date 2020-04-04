from rest_framework.fields import IntegerField

from lessons.utils.serializer import MatrixField
from lessons.utils.math import MatrixInt
from lessons.base import TaskBase, TaskSerializerBase


class TaskSerializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())


class Task(TaskBase):
    serializer = TaskSerializer

    text = 'Найти матрицу <formula>A^3</formula> и её след:'

    @property
    def matrix_a(self) -> MatrixInt:
        n = self.n
        return [
            [1, -2],
            [n - 10, -4],
        ]
