from rest_framework.fields import CharField

from lessons.base import TaskBase, TaskSerializerBase
from lessons.utils.serializer import MatrixField


class TaskSerializer(TaskSerializerBase):
    equation = MatrixField(child=CharField())


class Task(TaskBase):
    serializer = TaskSerializer

    text = 'Решить уравнение:'

    equation = [
        ['1', '1', '1'],
        ['1', '1-x', '1'],
        ['1', '1', '2-x'],
    ]
