from rest_framework.fields import IntegerField

from lessons.utils.serializer import MatrixField
from lessons.utils.math import MatrixStr
from lessons.base import TaskBase, TaskSerializerBase


class TaskSerializer(TaskSerializerBase):
    matrix_a = MatrixField(child=IntegerField())


class Task(TaskBase):
    serializer = TaskSerializer

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.equation = self._get_equation(self.n)

    def _get_text(self) -> str:
        return 'Решить уравнение:'

    def _get_equation(self, _: int) -> MatrixStr:
        return [
            ['1', '1', '1'],
            ['1', '1-x', '1'],
            ['1', '1', '2-x'],
        ]
