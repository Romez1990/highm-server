from typing import List, Tuple, Type, Optional, Dict, Mapping, Any
from django.http import Http404

from lessons.base import (
    LessonBase,
    LessonResultsBase,
    LessonResultsBaseSerializer,
)
from .l1.lesson import Lesson1
from .l1.lesson_results import Lesson1Results
from .l2.lesson import Lesson2
from .l2.lesson_results import Lesson2Results


class Lessons:
    lessons: List[Tuple[Type[LessonBase], Type[LessonResultsBase]]] = [
        (Lesson1, Lesson1Results),
        (Lesson2, Lesson2Results),
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

    @staticmethod
    def get_lesson_results_serializer(
        number: int,
        *args,
        **kwargs,
    ) -> Optional[LessonResultsBaseSerializer]:
        index = number - 1
        if index >= len(Lessons.lessons):
            return None
        _, lesson_results = Lessons.lessons[index]
        serializer_class = lesson_results.serializer
        return serializer_class(*args, **kwargs)

    @staticmethod
    def get_lesson_results_serializer_or_404(
        number: int,
        *args,
        **kwargs,
    ) -> LessonResultsBaseSerializer:
        serializer = Lessons.get_lesson_results_serializer(number, *args,
                                                           **kwargs)
        if serializer is None:
            raise Http404()
        return serializer

    @staticmethod
    def get_lesson_results(
        number: int,
        n: int,
        results: Dict[str, Mapping[str, Any]],
    ) -> Optional[LessonResultsBase]:
        index = number - 1
        if index >= len(Lessons.lessons):
            return None
        _, lesson_results = Lessons.lessons[index]
        return lesson_results(n, **results['answers'])

    @staticmethod
    def get_lesson_results_or_404(
        number: int,
        n: int,
        results: Dict[str, Mapping[str, Any]],
    ) -> LessonResultsBase:
        lesson_results = Lessons.get_lesson_results(number, n, results)
        if lesson_results is None:
            raise Http404()
        return lesson_results
