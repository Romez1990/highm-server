from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    IntegerField,
    BooleanField,
    ListField,
)

from .models import (
    LessonResult,
    TaskResult,
)


class LessonBasicSerializerBase(Serializer):
    title = CharField(max_length=150)


class LessonBasicSerializer(LessonBasicSerializerBase):
    passed = BooleanField()


class LessonSerializerBase(LessonBasicSerializerBase):
    goals = ListField(child=CharField(max_length=300))


class TaskSerializerBase(Serializer):
    text = CharField()


class LessonAnswersSerializerBase(Serializer):
    pass


class AnswerSerializerBase(Serializer):
    pass


class TaskResultSerializer(ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ['task_number', 'points', 'max_points']

    max_points = IntegerField()


class LessonResultSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['grade', 'points', 'max_points', 'task_results']

    task_results = TaskResultSerializer(many=True)
    max_points = IntegerField()
