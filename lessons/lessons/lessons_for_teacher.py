from typing import (
    List,
)

from lessons.base import (
    LessonBasicBase,
)
from .lessons_base import LessonsBase


class LessonsForTeacher(LessonsBase):
    @staticmethod
    def number_of_lessons() -> int:
        return len(LessonsForTeacher._lessons)

    @staticmethod
    def get_list() -> List[LessonBasicBase]:
        return [lesson.LessonBasic(number)
                for number, lesson in enumerate(LessonsForTeacher._lessons, 1)]
