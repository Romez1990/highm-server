from typing import List

from .task_base import TaskBase


class LessonBase:
    title: str = 'None'
    goals: List[str] = ['None']
    tasks: List[TaskBase] = []
