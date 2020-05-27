from typing import (
    List,
)


class LessonBaseBase:
    title: str


class LessonBasicBase(LessonBaseBase):
    pass


class LessonBase(LessonBaseBase):
    goals: List[str] = []
