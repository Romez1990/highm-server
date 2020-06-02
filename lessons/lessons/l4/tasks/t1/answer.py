from typing import (
    Dict,
    List,
    Any,
)
from rest_framework.serializers import (
    Serializer,
    FloatField,
    ListField,
)

from lessons.base import AnswerBase
from lessons.serializers_for_student import AnswerSerializerBase
from .task import Task1
from .steps.s1 import Step1
from .steps.s2 import Step2
from .steps.s3 import Step3


class IntermediateResultsSerializer(Serializer):
    x = FloatField()
    y = FloatField()


class Answer1Serializer(AnswerSerializerBase):
    intermediate_results = ListField(child=IntermediateResultsSerializer(),
                                     min_length=Task1.N, max_length=Task1.N)
    result = FloatField()


class Answer1(AnswerBase):
    _task_class = Task1
    _step_classes = [
        Step1,
        Step2,
        Step3,
    ]

    def __init__(
            self,
            n: int,
            result: float,
            intermediate_results: List[Dict[str, float]],
    ) -> None:
        super().__init__(n)
        self.intermediate_results = intermediate_results
        self.result = result

    def to_json(self) -> Dict[str, Any]:
        return {
            'intermediate_results': self.intermediate_results,
            'result': self.result,
        }
