from ..t1.answer import Answer1Serializer, Answer1
from .task import Task2


class Answer2Serializer(Answer1Serializer):
    pass


class Answer2(Answer1):
    _task_class = Task2
