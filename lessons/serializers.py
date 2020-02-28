from typing import List
from rest_framework.serializers import (
    Serializer,
    CharField,
    ListField,
    SerializerMethodField,
)

from .lesson_base import LessonBase
from .task_base import TaskBase


class LessonSerializer(Serializer):
    title = CharField(max_length=150)


class LessonDetailsSerializer(Serializer):
    title = CharField(max_length=150)
    goals = ListField(child=CharField(max_length=300))
    tasks = SerializerMethodField()

    def get_tasks(self, lesson: LessonBase) -> List[TaskBase]:
        tasks: List[TaskBase] = []
        for task in lesson.tasks:
            serializer = task.given_serializer(task, context=self.context)
            tasks.append(serializer.data)
        return tasks
