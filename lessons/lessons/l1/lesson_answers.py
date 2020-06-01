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
from .tasks.t2.answer import Answer2, Answer2Serializer
from .tasks.t3.answer import Answer3, Answer3Serializer
from .tasks.t4.answer import Answer4, Answer4Serializer
from .tasks.t5.answer import Answer5, Answer5Serializer
from .tasks.t6.answer import Answer6, Answer6Serializer


class AnswersSerializer(Serializer):
    answer1 = Answer1Serializer()
    answer2 = Answer2Serializer()
    answer3 = Answer3Serializer()
    answer4 = Answer4Serializer()
    answer5 = Answer5Serializer()
    answer6 = Answer6Serializer()


class Lesson1AnswerSerializer(LessonAnswersSerializerBase):
    answers = AnswersSerializer()


class Lesson1Answers(LessonAnswersBase):
    _answer_classes = [
        Answer1,
        Answer2,
        Answer3,
        Answer4,
        Answer5,
        Answer6,
    ]

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
        self._answers = {
            'answer1': Answer1(n, **answer1),
            'answer2': Answer2(n, **answer2),
            'answer3': Answer3(n, **answer3),
            'answer4': Answer4(n, **answer4),
            'answer5': Answer5(n, **answer5),
            'answer6': Answer6(n, **answer6),
        }

    grades_and_minimal_points = [
        (5, 12),
        (4, 10),
        (3, 7),
    ]
