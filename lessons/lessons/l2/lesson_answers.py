from typing import (
    Mapping,
    Any,
)
from rest_framework.serializers import Serializer

from lessons.serializers_for_student import LessonAnswersSerializerBase
from lessons.base import LessonAnswersBase
from .tasks.t1.answer import Answer1, Answer1Serializer
from .tasks.t2.answer import Answer2, Answer2Serializer


class AnswersSerializer(Serializer):
    answer1 = Answer1Serializer()
    answer2 = Answer2Serializer()


class Lesson2AnswerSerializer(LessonAnswersSerializerBase):
    answers = AnswersSerializer()


class Lesson2Answers(LessonAnswersBase):
    _answer_classes = [
        Answer1,
        Answer2,
    ]

    def __init__(
            self,
            n: int,
            answer1: Mapping[str, Any],
            answer2: Mapping[str, Any],
    ) -> None:
        super().__init__(n)
        self._answers = {
            'answer1': Answer1(n, **answer1),
            'answer2': Answer2(n, **answer2),
        }

    grades_and_minimal_points = [
        (5, 2),
        (4, 1),
    ]
