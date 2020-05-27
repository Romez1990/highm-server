from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    IntegerField,
)

from .models import (
    LessonResult,
)


class LessonBasicSerializer(Serializer):
    title = CharField(max_length=150)


class LessonResultSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['id', 'student_id', 'n', 'grade', 'points', 'max_points']

    max_points = IntegerField()
