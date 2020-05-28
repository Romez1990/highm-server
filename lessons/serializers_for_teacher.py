from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    IntegerField,
)

from .models import (
    TaskResult,
    LessonResult,
)


class LessonBasicSerializer(Serializer):
    title = CharField(max_length=150)


class LessonResultSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['id', 'student_id', 'n', 'grade', 'points', 'max_points']

    max_points = IntegerField()


class TaskResultSerializer(ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ['points', 'max_points', 'answer']


class LessonResultAnswersSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['task_results']

    task_results = TaskResultSerializer(many=True)
