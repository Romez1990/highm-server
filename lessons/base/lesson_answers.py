from typing import (
    List,
    Dict,
    Tuple,
    Optional,
    Iterable,
    Mapping,
    Type,
    Any,
)

from .answer import AnswerBase


class LessonAnswersBase:
    _answer_classes: List[Type[AnswerBase]]
    _answers: Dict[str, AnswerBase]

    @property
    def answers(self) -> Iterable[AnswerBase]:
        return self._answers.values()

    def __init__(self, n: int, **kwargs: Dict[str, Mapping[str, Any]]) -> None:
        self.n = n
        self._points: Optional[int] = None

    def check(self) -> None:
        for answer in self._answers.values():
            answer.check()

    @property
    def points(self) -> int:
        if self._points is None:
            self._points = sum(answer.points
                               for answer in self._answers.values())
        return self._points

    grades_and_minimal_points: List[Tuple[int, int]]

    @classmethod
    def max_points(cls) -> int:
        return sum(answer.max_points() for answer in cls._answer_classes)

    @classmethod
    def task_max_points(cls, task_number: int) -> int:
        task_index = task_number - 1
        answer = cls._answer_classes[task_index]
        return answer.max_points()

    @property
    def grade(self) -> int:
        for grade, minimal_points in self.grades_and_minimal_points:
            if self.points >= minimal_points:
                return grade
        return 2
