from rest_framework.serializers import (
    Serializer,
    CharField,
    ListField,
)


class LessonBasicSerializerBase(Serializer):
    title = CharField(max_length=150)


class LessonBasicSerializer(LessonBasicSerializerBase):
    pass


class LessonSerializerBase(LessonBasicSerializerBase):
    goals = ListField(child=CharField(max_length=300))


class TaskSerializerBase(Serializer):
    text = CharField()
