from typing import List, Type

from lessons.base import (
    LessonBase,
)
from .l1.lesson import Lesson1
from .l2.lesson import Lesson2


class Lessons:
    lessons: List[Type[LessonBase]] = [
        Lesson1,
        Lesson2,
    ]

    @staticmethod
    def get_lesson_list() -> List[Type[LessonBase]]:
        return [lesson for lesson, _ in Lessons.lessons]
