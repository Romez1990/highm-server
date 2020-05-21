from typing import Mapping, Any
from rest_framework.serializers import Serializer

from lessons.base import (
    LessonAnswersBase,
    LessonAnswersBaseSerializer,
)
from .tasks.t1.answer import Answer1, Answer1Serializer
from .tasks.t2.answer import Answer2, Answer2Serializer
# from .tasks.t3.answer import Answer3, Answer3Serializer


class Lesson2AnswersSerializer(Serializer):
    answer1 = Answer1Serializer()
    answer2 = Answer2Serializer()
    # answer3 = Answer3Serializer()


class Lesson2AnswerSerializer(LessonAnswersBaseSerializer):
    answers = Lesson2AnswersSerializer()


class Lesson2Answers(LessonAnswersBase):
    serializer = Lesson2AnswerSerializer

    def __init__(
        self,
        n: int,
        answer1: Mapping[str, Any],
        answer2: Mapping[str, Any],
        # answer3: Mapping[str, Any],
    ) -> None:
        super().__init__(n)
        self.answers = {
            'answer1': Answer1(n, **answer1),
            'answer2': Answer2(n, **answer2),
            # 'answer3': Answer3(n, **answer3),
        }
