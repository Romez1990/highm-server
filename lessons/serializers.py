from rest_framework.serializers import (
    ModelSerializer,
)

from .models import (
    TaskResult,
    LessonResult,
)


class TaskResultSerializer(ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ['task_number', 'right']


class LessonResultSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['grade', 'task_results']

    task_results = TaskResultSerializer(many=True)
