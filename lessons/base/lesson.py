from typing import List, Type

from .task import TaskBase
from .task_answer import TaskAnswerBase


class LessonBase:
    title: str = 'None'
    goals: List[str] = ['None']
    tasks: List[Type[TaskBase]] = []
    task_answers: List[Type[TaskAnswerBase]] = []
