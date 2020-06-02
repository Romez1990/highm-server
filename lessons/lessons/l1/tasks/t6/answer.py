from ..t3.answer import Answer3Serializer, Answer3
from .task import Task6
from .steps.s1 import Step1


class Answer6Serializer(Answer3Serializer):
    pass


class Answer6(Answer3):
    _task_class = Task6
    _task: Task6
    _step_classes = [
        Step1,
    ]
