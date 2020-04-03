from typing import Type
from rest_framework.serializers import Serializer
from rest_framework.fields import CharField


class TaskSerializerBase(Serializer):
    text = CharField()


class TaskBase:
    serializer: Type[TaskSerializerBase]

    def __init__(self, n: int) -> None:
        self.n = n
        self.text = self._get_text()

    def _get_text(self) -> str:
        raise NotImplementedError
