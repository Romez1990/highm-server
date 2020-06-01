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
from .tasks.t3.task import Task3, Task3Serializer
from .tasks.t4.task import Task4, Task4Serializer
from .tasks.t5.task import Task5, Task5Serializer
from .tasks.t6.task import Task6, Task6Serializer


class TasksSerializer(Serializer):
    task1 = Task1Serializer()
    task2 = Task2Serializer()
    task3 = Task3Serializer()
    task4 = Task4Serializer()
    task5 = Task5Serializer()
    task6 = Task6Serializer()


class Lesson1Serializer(LessonSerializerBase):
    tasks = TasksSerializer()


class Lesson1BasicBase(LessonBaseBase):
    title = 'Выполнение действий с матрицами. Вычисление определителя матрицы.'


class Lesson1Basic(Lesson1BasicBase, LessonBasicBase):
    pass


class Lesson1(Lesson1BasicBase, LessonBase):
    goals = [
        'получить навыки выполнения операций над матрицами и вычисления '
        'определителей квадратных матриц различных порядков',
        'закрепить теоретические и практические знания и навыки по данной теме',
    ]

    def __init__(
            self,
            n: int,
    ) -> None:
        super().__init__(n)
        self.tasks = {
            'task1': Task1(n),
            'task2': Task2(n),
            'task3': Task3(n),
            'task4': Task4(n),
            'task5': Task5(n),
            'task6': Task6(n),
        }
