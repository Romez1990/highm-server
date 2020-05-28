from typing import (
    List,
    Type,
    NamedTuple,
)
from rest_framework.exceptions import (
    NotFound,
)

from lessons.serializers_for_student import (
    LessonSerializerBase,
    LessonAnswersSerializerBase,
)
from lessons.base import (
    LessonBasicBase,
    LessonBase,
    LessonAnswersBase,
)
from .l1.lesson import (
    Lesson1Basic,
    Lesson1,
    Lesson1Serializer,
)
from .l1.lesson_answers import (
    Lesson1Answers,
    Lesson1AnswerSerializer,
)
from .l2.lesson import (
    Lesson2Basic,
    Lesson2,
    Lesson2Serializer,
)
from .l2.lesson_answers import (
    Lesson2Answers,
    Lesson2AnswerSerializer,
)


class Lesson(NamedTuple):
    LessonBasic: Type[LessonBasicBase]
    Lesson: Type[LessonBase]
    LessonSerializer: Type[LessonSerializerBase]
    LessonAnswers: Type[LessonAnswersBase]
    LessonAnswersSerializer: Type[LessonAnswersSerializerBase]


class LessonsBase:
    _lessons: List[Lesson] = [
        Lesson(Lesson1Basic, Lesson1, Lesson1Serializer, Lesson1Answers,
               Lesson1AnswerSerializer),
        Lesson(Lesson2Basic, Lesson2, Lesson2Serializer, Lesson2Answers,
               Lesson2AnswerSerializer),
    ]

    @staticmethod
    def lesson_exists(number: int) -> bool:
        return 1 <= number <= len(LessonsBase._lessons)

    @staticmethod
    def lesson_exists_of_404(number: int) -> None:
        if not LessonsBase.lesson_exists(number):
            raise NotFound('Lesson not found.')
