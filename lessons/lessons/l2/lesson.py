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
from .tasks.t2.task import Task2, Task2Serializer


class TasksSerializer(Serializer):
    task1 = Task1Serializer()
    task2 = Task2Serializer()


class Lesson2Serializer(LessonSerializerBase):
    tasks = TasksSerializer()


class Lesson2BasicBase(LessonBaseBase):
    title = 'Решение систем линейных уравнений методом Крамера, матричным ' \
            'способом, методом Гаусса.'


class Lesson2Basic(Lesson2BasicBase, LessonBasicBase):
    pass


class Lesson2(Lesson2BasicBase, LessonBase):
    goals = [
        'получить навыки решения систем n линейных уравнений с n переменными',
        'закрепить теоретические и практические знания и навыки по данной теме',
    ]

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.tasks = {
            'task1': Task1(n),
            'task2': Task2(n),
        }
