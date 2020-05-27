from typing import (
    List,
    Type,
    Optional,
    Dict,
    Mapping,
    Any,
)
from rest_framework.exceptions import (
    NotFound,
)

from users.models import Student
from lessons.serializers_for_student import (
    LessonSerializerBase,
    LessonAnswersSerializerBase,
)
from lessons.base import (
    LessonBasicBase,
    LessonBase,
    LessonAnswersBase,
)
from .lessons_base import LessonsBase


class LessonsForStudent(LessonsBase):
    @staticmethod
    def get_list(student: Student) -> List[LessonBasicBase]:
        return [lesson.LessonBasic(number, student)
                for number, lesson in enumerate(LessonsForStudent._lessons, 1)]

    @staticmethod
    def get_lesson(number: int, n: int) -> Optional[LessonBase]:
        index = number - 1
        if index >= len(LessonsForStudent._lessons):
            return None
        lesson = LessonsForStudent._lessons[index]
        return lesson.Lesson(n)

    @staticmethod
    def get_lesson_or_404(number: int, n: int) -> LessonBase:
        lesson = LessonsForStudent.get_lesson(number, n)
        if lesson is None:
            raise NotFound('Lesson not found.')
        return lesson

    @staticmethod
    def get_lesson_serializer_class(number: int) -> Type[LessonSerializerBase]:
        index = number - 1
        if index >= len(LessonsForStudent._lessons):
            raise ValueError(f'Lesson{number}Serializer not found')
        lesson = LessonsForStudent._lessons[index]
        return lesson.LessonSerializer

    @staticmethod
    def get_answers(
            number: int,
            n: int,
            answers: Dict[str, Mapping[str, Any]]
    ) -> Optional[LessonAnswersBase]:
        index = number - 1
        if index >= len(LessonsForStudent._lessons):
            return None
        lesson = LessonsForStudent._lessons[index]
        return lesson.LessonAnswers(n, **answers['answers'])

    @staticmethod
    def get_answers_or_404(
            number: int,
            n: int,
            answers: Dict[str, Mapping[str, Any]]
    ) -> LessonAnswersBase:
        lesson_answers = LessonsForStudent.get_answers(number, n, answers)
        if lesson_answers is None:
            raise NotFound('LessonResults not found.')
        return lesson_answers

    @staticmethod
    def get_lesson_answers_serializer_class(
            number: int) -> Type[LessonAnswersSerializerBase]:
        index = number - 1
        if index >= len(LessonsForStudent._lessons):
            raise ValueError(f'Lesson{number}AnswersSerializer not found')
        lesson = LessonsForStudent._lessons[index]
        return lesson.LessonAnswersSerializer

    @staticmethod
    def lesson_max_points(lesson_number: int) -> int:
        lesson_index = lesson_number - 1
        lesson = LessonsForStudent._lessons[lesson_index]
        return lesson.LessonAnswers.max_points()

    @staticmethod
    def task_max_points(lesson_number: int, task_number: int) -> int:
        lesson_index = lesson_number - 1
        lesson = LessonsForStudent._lessons[lesson_index]
        return lesson.LessonAnswers.task_max_points(task_number)
