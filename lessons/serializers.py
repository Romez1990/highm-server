from rest_framework.serializers import (
    Serializer,
    CharField,
)


class LessonBasicSerializerBase(Serializer):
    title = CharField(max_length=150)


class LessonBasicSerializer(LessonBasicSerializerBase):
    pass
