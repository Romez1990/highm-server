from rest_framework.serializers import (
    Serializer,
)

from lessons.serializers_for_student import LessonSerializerBase
from lessons.base import (
    LessonBaseBase,
    LessonBasicBase,
    LessonBase,
)
from .tasks.t1.task import Task1, Task1Serializer


class TasksSerializer(Serializer):
    task1 = Task1Serializer()


class Lesson3Serializer(LessonSerializerBase):
    tasks = TasksSerializer()


class Lesson3BasicBase(LessonBaseBase):
    title = 'Применение метода половинного деления (метод дихотомии).'


class Lesson3Basic(Lesson3BasicBase, LessonBasicBase):
    pass


class Lesson3(Lesson3BasicBase, LessonBase):
    goals = [
        'научиться применять метод половинного деления при решении уравнений',
        'закрепить теоретические и практические знания и навыки по данной теме',
    ]

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.tasks = {
            'task1': Task1(n),
        }
