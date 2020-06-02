from numpy import sqrt

from ..t1.task import Task1Serializer, Task1


class Task2Serializer(Task1Serializer):
    pass


class Task2(Task1):
    @property
    def text(self) -> str:
        N = self.N
        return f'Вычислить значение интеграла по формуле трапеций при n = {N}:'

    def f(self, x: float) -> float:
        n = self.n
        return sqrt(n * x - 0.1)

    @property
    def integral(self) -> str:
        n = self.n
        return self._integral_wrap(r'\sqrt{%sx - 0.1}' % n)

    N = 8
