from typing import (
    Dict,
    Any,
)
from rest_framework.fields import (
    ChoiceField,
    IntegerField,
)

from lessons.base import AnswerBase
from lessons.utils.math import MatrixInt
from lessons.utils.serializer import MatrixField
from lessons.serializers import AnswerSerializerBase
from .task import Task1
from .steps.s1 import Step1
from .steps.s2 import Step2


class Answer1Serializer(AnswerSerializerBase):
    which_of_products = ChoiceField(['AB', 'BA'])
    product = MatrixField(child=IntegerField())


class Answer1(AnswerBase):
    _task_type = Task1
    task: Task1
    _step_classes = [
        Step1,
        Step2,
    ]

    def __init__(
            self,
            n: int,
            which_of_products: str,
            product: MatrixInt,
    ) -> None:
        super().__init__(n)
        self.which_of_products = which_of_products
        self.product = product

    def to_json(self) -> Dict[str, Any]:
        return {
            'which_of_products': self.which_of_products,
            'product': self.product,
        }
