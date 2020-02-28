from typing import List
from rest_framework.serializers import Serializer
from rest_framework.fields import (
    CharField,
    IntegerField,
    ChoiceField,
    ListField,
    HiddenField,
    CurrentUserDefault,
    SerializerMethodField,
)

from .given import get_matrix_a


def get_n(request) -> int:
    return request.user.student.n


class TaskGivenSerializer(Serializer):
    text = CharField()
    matrix_a = SerializerMethodField()

    def get_matrix_a(self, task) -> List[List[int]]:
        n = get_n(self.context['request'])
        return get_matrix_a(n)


class TaskResultSerializer(Serializer):
    user = HiddenField(default=CurrentUserDefault())
    n = IntegerField(source='user.student.n', read_only=True)
    product = ListField(child=ListField(child=IntegerField()))
