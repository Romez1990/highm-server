from typing import (
    List,
)

from lessons.base import (
    LessonBasicBase,
)
from .lessons_base import LessonsBase


class LessonsForTeacher(LessonsBase):
    @staticmethod
    def get_list() -> List[LessonBasicBase]:
        return [lesson.LessonBasic(number)
                for number, lesson in enumerate(LessonsForTeacher._lessons, 1)]
