from rest_framework.serializers import Serializer

from lessons.base import (
    LessonBaseSerializer,
    LessonBase,
)
from .tasks.t1.task import Task1, Task1Serializer
from .tasks.t2.task import Task2, Task2Serializer
# from .tasks.t3.task import Task3, Task3Serializer


class Lesson2TasksSerializer(Serializer):
    task1 = Task1Serializer()
    task2 = Task2Serializer()
    # task3 = Task3Serializer()


class Lesson2Serializer(LessonBaseSerializer):
    tasks = Lesson2TasksSerializer()


class Lesson2(LessonBase):
    serializer = Lesson2Serializer
    title = 'Решение систем линейных уравнений методом Крамера, матричным ' \
            'способом, методом Гаусса.'
    goals = [
        'получить навыки решения систем n линейных уравнений с n переменными',
        'закрепить теоретические и практические знания и навыки по данной теме',
    ]

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.tasks = {
            'task1': Task1(n),
            'task2': Task2(n),
            # 'task3': Task3(n),
        }
