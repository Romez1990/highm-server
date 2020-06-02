from lessons.utils.math import MatrixInt
from ..t3.task import Task3Serializer, Task3


class Task6Serializer(Task3Serializer):
    pass


class Task6(Task3):
    text = 'Вычислить определитель матрицы четвёртого порядка:'

    @property
    def matrix_a(self) -> MatrixInt:
        n = self.n
        return [
            [0, 1, 1, n - 10],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [n - 20, 1, 1, 0],
        ]
