from typing import (
    List,
    Type,
    NamedTuple,
)

from lessons.base import (
    LessonBasicBase,
)
from .l1.lesson import (
    Lesson1Basic,
)


class Lesson(NamedTuple):
    LessonBasic: Type[LessonBasicBase]


class Lessons:
    _lessons: List[Lesson] = [
        Lesson(Lesson1Basic),
    ]

    @staticmethod
    def get_list() -> List[LessonBasicBase]:
        return [lesson.LessonBasic() for lesson in Lessons._lessons]
