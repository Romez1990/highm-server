from typing import Mapping, Any
from rest_framework.serializers import Serializer

from lessons.base import (
    LessonAnswersBaseSerializer,
    LessonAnswersBase,
)
from .tasks.t1.answer import Answer1, Answer1Serializer
from .tasks.t2.answer import Answer2, Answer2Serializer
from .tasks.t3.answer import Answer3, Answer3Serializer
from .tasks.t4.answer import Answer4, Answer4Serializer
from .tasks.t5.answer import Answer5, Answer5Serializer
from .tasks.t6.answer import Answer6, Answer6Serializer


class Lesson1AnswersSerializer(Serializer):
    answer1 = Answer1Serializer()
    answer2 = Answer2Serializer()
    answer3 = Answer3Serializer()
    answer4 = Answer4Serializer()
    answer5 = Answer5Serializer()
    answer6 = Answer6Serializer()


class Lesson1AnswerSerializer(LessonAnswersBaseSerializer):
    answers = Lesson1AnswersSerializer()


class Lesson1Answers(LessonAnswersBase):
    serializer = Lesson1AnswerSerializer

    def __init__(
        self,
        n: int,
        answer1: Mapping[str, Any],
        answer2: Mapping[str, Any],
        answer3: Mapping[str, Any],
        answer4: Mapping[str, Any],
        answer5: Mapping[str, Any],
        answer6: Mapping[str, Any],
    ) -> None:
        super().__init__(n)
        self.answers = {
            'answer1': Answer1(n, **answer1),
            'answer2': Answer2(n, **answer2),
            'answer3': Answer3(n, **answer3),
            'answer4': Answer4(n, **answer4),
            'answer5': Answer5(n, **answer5),
            'answer6': Answer6(n, **answer6),
        }
