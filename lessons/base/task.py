from rest_framework.serializers import Serializer
from rest_framework.fields import CharField


class TaskSerializerBase(Serializer):
    text = CharField()


class TaskBase:
    def __init__(self, n: int) -> None:
        self.n = n

    text: str
