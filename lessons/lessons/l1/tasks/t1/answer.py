from rest_framework.fields import (
    ChoiceField,
    IntegerField,
)

from lessons.base import AnswerBase, AnswerSerializerBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from .task import Task


class TaskResultSerializer(AnswerSerializerBase):
    which_of_products = ChoiceField(['AB', 'BA'])
    product = MatrixField(child=IntegerField())


class Answer(AnswerBase):
    serializer = TaskResultSerializer
    task_type = Task

    def __init__(
        self,
        n: int,
        which_of_products: str,
        product: MatrixInt,
    ) -> None:
        super().__init__(n)
        self.which_of_products = which_of_products
        self.product = product
