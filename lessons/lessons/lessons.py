from typing import (
    List,
    Type,
    Optional,
    NamedTuple,
)
from rest_framework.exceptions import (
    NotFound,
)

from lessons.serializers import (
    LessonSerializerBase,
)
from lessons.base import (
    LessonBasicBase,
    LessonBase,
)
from .l1.lesson import (
    Lesson1Basic,
    Lesson1,
    Lesson1Serializer,
)


class Lesson(NamedTuple):
    LessonBasic: Type[LessonBasicBase]
    Lesson: Type[LessonBase]
    LessonSerializer: Type[LessonSerializerBase]


class Lessons:
    _lessons: List[Lesson] = [
        Lesson(Lesson1Basic, Lesson1, Lesson1Serializer),
    ]

    @staticmethod
    def get_list() -> List[LessonBasicBase]:
        return [lesson.LessonBasic() for lesson in Lessons._lessons]

    @staticmethod
    def get_lesson(number: int, n: int) -> Optional[LessonBase]:
        index = number - 1
        if index >= len(Lessons._lessons):
            return None
        lesson = Lessons._lessons[index]
        return lesson.Lesson(n)

    @staticmethod
    def get_lesson_or_404(number: int, n: int) -> LessonBase:
        lesson = Lessons.get_lesson(number, n)
        if lesson is None:
            raise NotFound('Lesson not found.')
        return lesson

    @staticmethod
    def get_lesson_serializer_class(number: int) -> Type[LessonSerializerBase]:
        index = number - 1
        if index >= len(Lessons._lessons):
            raise ValueError(f'Lesson{number}Serializer not found')
        lesson = Lessons._lessons[index]
        return lesson.LessonSerializer
