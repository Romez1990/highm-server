from rest_framework.serializers import (
    Serializer,
    CharField,
)


class LessonBasicSerializer(Serializer):
    title = CharField(max_length=150)
