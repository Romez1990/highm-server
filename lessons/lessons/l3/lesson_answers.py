from typing import (
    Mapping,
    Any,
)
from rest_framework.serializers import (
    Serializer,
)

from lessons.serializers_for_student import LessonAnswersSerializerBase
from lessons.base import LessonAnswersBase
from .tasks.t1.answer import Answer1, Answer1Serializer


class AnswersSerializer(Serializer):
    answer1 = Answer1Serializer()


class Lesson3AnswerSerializer(LessonAnswersSerializerBase):
    answers = AnswersSerializer()


class Lesson3Answers(LessonAnswersBase):
    _answer_classes = [
        Answer1,
    ]

    def __init__(
            self,
            n: int,
            answer1: Mapping[str, Any],
    ) -> None:
        super().__init__(n)
        self._answers = {
            'answer1': Answer1(n, **answer1),
        }

    grades_and_minimal_points = [
        (5, 3),
        (4, 2),
        (3, 1),
    ]
