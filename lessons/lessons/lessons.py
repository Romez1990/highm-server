from typing import List, Type, Optional
from django.http import Http404

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

    @staticmethod
    def get_lesson(number: int, n: int) -> Optional[LessonBase]:
        index = number - 1
        if index >= len(Lessons.lessons):
            return None
        lesson, _ = Lessons.lessons[index]
        return lesson(n)

    @staticmethod
    def get_lesson_or_404(number: int, n: int) -> LessonBase:
        lesson = Lessons.get_lesson(number, n)
        if lesson is None:
            raise Http404()
        return lesson
