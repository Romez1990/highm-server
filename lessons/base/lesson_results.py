from typing import Dict, Type, Mapping, Any
from rest_framework.serializers import Serializer

from .answer import AnswerBase


class LessonResultsBaseSerializer(Serializer):
    pass


class LessonResultsBase:
    serializer: Type[LessonResultsBaseSerializer]
    answers: Dict[str, AnswerBase]

    def __init__(self, n: int, **kwargs: Dict[str, Mapping[str, Any]]) -> None:
        self.n = n

    def check(self) -> Dict[str, bool]:
        return {name: answer.check() for name, answer in self.answers.items()}
