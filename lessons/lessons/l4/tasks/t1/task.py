from rest_framework.serializers import (
    CharField,
    IntegerField,
)
from numpy import log

from lessons.base import TaskBase
from lessons.serializers_for_student import TaskSerializerBase


class Task1Serializer(TaskSerializerBase):
    integral = CharField()
    tolerance = IntegerField()


class Task1(TaskBase):
    @property
    def text(self) -> str:
        N = self.N
        return f'Найти значение интеграла по формуле трапеций при n = {N}:'

    @property
    def a(self) -> float:
        n = self.n
        return float(f'0.{n}')

    @property
    def b(self) -> float:
        n = self.n
        return float(f'{n}.6')

    def f(self, x: float) -> float:
        n = self.n
        return log(x + n) / x

    @property
    def integral(self) -> str:
        n = self.n
        return self._integral_wrap(r'\frac{\ln{(x + %s)}}{x}' % n)

    def _integral_wrap(self, expression: str) -> str:
        a = self.a
        b = self.b
        return r'\int_{%s}^{%s} %s dx' % (a, b, expression)

    N = 10

    tolerance = 5  # decimal places
