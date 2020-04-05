from typing import List, Type

from .task import TaskBase
from .answer import AnswerBase


class LessonBase:
    title: str = 'None'
    goals: List[str] = ['None']
    tasks: List[Type[TaskBase]] = []
    answers: List[Type[AnswerBase]] = []
