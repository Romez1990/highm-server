from typing import List, Tuple, Type, Optional, Dict, Mapping, Any
from django.http import Http404

from users.models import Student
from lessons.base import (
    LessonBase,
    LessonBasicBase,
    LessonAnswersBase,
    LessonAnswersBaseSerializer,
)
from .l1.lesson import Lesson1, Lesson1Basic
from .l1.lesson_answers import Lesson1Answers
from .l2.lesson import Lesson2, Lesson2Basic
from .l2.lesson_answers import Lesson2Answers


class Lessons:
    lessons: List[Tuple[
        Type[LessonBasicBase], Type[LessonBase], Type[LessonAnswersBase]]] = [
        (Lesson1Basic, Lesson1, Lesson1Answers),
        (Lesson2Basic, Lesson2, Lesson2Answers),
    ]

    @staticmethod
    def get_lesson_list(student: Student) -> List[LessonBasicBase]:
        return [lesson_basic(student) for lesson_basic, _, _ in Lessons.lessons]

    @staticmethod
    def get_lesson(number: int, n: int) -> Optional[LessonBase]:
        index = number - 1
        if index >= len(Lessons.lessons):
            return None
        _, lesson, _ = Lessons.lessons[index]
        return lesson(n)

    @staticmethod
    def get_lesson_or_404(number: int, n: int) -> LessonBase:
        lesson = Lessons.get_lesson(number, n)
        if lesson is None:
            raise Http404()
        return lesson

    @staticmethod
    def get_lesson_answers_serializer(
        number: int,
        *args,
        **kwargs,
    ) -> Optional[LessonAnswersBaseSerializer]:
        index = number - 1
        if index >= len(Lessons.lessons):
            return None
        _, _, lesson_answers = Lessons.lessons[index]
        serializer_class = lesson_answers.serializer
        return serializer_class(*args, **kwargs)

    @staticmethod
    def get_lesson_answers_serializer_or_404(
        number: int,
        *args,
        **kwargs,
    ) -> LessonAnswersBaseSerializer:
        serializer = Lessons.get_lesson_answers_serializer(number, *args,
                                                           **kwargs)
        if serializer is None:
            raise Http404()
        return serializer

    @staticmethod
    def get_lesson_answers(
        number: int,
        n: int,
        answers: Dict[str, Mapping[str, Any]],
    ) -> Optional[LessonAnswersBase]:
        index = number - 1
        if index >= len(Lessons.lessons):
            return None
        _, _, lesson_answers = Lessons.lessons[index]
        return lesson_answers(n, **answers['answers'])

    @staticmethod
    def get_lesson_answers_or_404(
        number: int,
        n: int,
        answers: Dict[str, Mapping[str, Any]],
    ) -> LessonAnswersBase:
        lesson_answers = Lessons.get_lesson_answers(number, n, answers)
        if lesson_answers is None:
            raise Http404()
        return lesson_answers