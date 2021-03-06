from rest_framework.serializers import (
    CharField,
    IntegerField,
)
from numpy import pi, cos

from lessons.base import TaskBase
from lessons.serializers_for_student import TaskSerializerBase


class Task1Serializer(TaskSerializerBase):
    equation = CharField(source='equation_formula')
    a = CharField(source='a_formula')
    b = CharField(source='b_formula')
    epsilon = CharField(source='epsilon_formula')
    tolerance = IntegerField()


class Task1(TaskBase):
    text = r'Найти корень <formula>\xi</formula> уравнения на отрезке ' \
           '<formula>[a,b]</formula> с заданной погрешностью ' \
           r'<formula>\epsilon</formula> методом половинного деления:'

    @property
    def coefficient(self) -> float:
        n = self.n
        return 0.21 * n + 1.5

    def equation(self, x: float) -> float:
        coefficient = self.coefficient
        return coefficient * cos(x) - x ** 2

    @property
    def equation_formula(self) -> str:
        coefficient = self.coefficient
        return fr'{coefficient}\cos x - x^2 = 0'

    a = pi / 4
    b = pi / 2

    a_formula = r'\frac{\pi}{4}'
    b_formula = r'\frac{\pi}{2}'

    epsilon = 1.e-3
    epsilon_formula = '10^{-3}'

    tolerance = 6  # decimal places
