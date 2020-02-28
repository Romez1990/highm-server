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

from .given import get_matrix_a, get_matrix_b


def get_n(request) -> int:
    return request.user.student.n


class TaskGivenSerializer(Serializer):
    text = CharField()
    matrix_a = SerializerMethodField()
    matrix_b = SerializerMethodField()

    def get_matrix_a(self, _) -> List[List[int]]:
        n = get_n(self.context['request'])
        return get_matrix_a(n)

    def get_matrix_b(self, _) -> List[List[int]]:
        n = get_n(self.context['request'])
        return get_matrix_b(n)


class TaskResultSerializer(Serializer):
    user = HiddenField(default=CurrentUserDefault())
    n = IntegerField(source='user.student.n', read_only=True)
    which_of_products = ChoiceField(['AB', 'BA'])
    product = ListField(child=ListField(child=IntegerField()))
