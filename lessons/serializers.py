from typing import List
from rest_framework.serializers import (
    Serializer,
    CharField,
    ListField,
    SerializerMethodField,
)
from rest_framework.utils.serializer_helpers import ReturnDict

from lessons.utils.serializer import get_n
from lessons.base import LessonBase


class LessonSerializer(Serializer):
    title = CharField(max_length=150)


class LessonDetailsSerializer(Serializer):
    title = CharField(max_length=150)
    goals = ListField(child=CharField(max_length=300))
    tasks = SerializerMethodField()

    def get_tasks(self, lesson: LessonBase) -> List[ReturnDict]:
        n = get_n(self)
        tasks: List[ReturnDict] = []
        for Task in lesson.tasks:
            serializer = Task.serializer(Task(n), context=self.context)
            tasks.append(serializer.data)
        return tasks
