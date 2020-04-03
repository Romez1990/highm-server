from rest_framework.fields import IntegerField

from lessons.utils.serializer import MatrixField
from lessons.utils.math import MatrixInt
from lessons.base import TaskBase, TaskSerializerBase


class TaskSerializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())


class Task(TaskBase):
    serializer = TaskSerializer

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.matrix_a = self._get_matrix_a(self.n)

    def _get_text(self) -> str:
        return 'Найти матрицу <formula>A^3</formula> и её след:'

    def _get_matrix_a(self, n: int) -> MatrixInt:
        return [
            [1, -2],
            [n - 10, -4],
        ]
