from typing import (
    List,
    Dict,
)

from .task import TaskBase


class LessonBaseBase:
    title: str


class LessonBasicBase(LessonBaseBase):
    pass


class LessonBase(LessonBaseBase):
    goals: List[str]
    tasks: Dict[str, TaskBase]

    def __init__(self, n: int) -> None:
        self.n = n
