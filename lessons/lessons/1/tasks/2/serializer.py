from typing import List
from rest_framework.serializers import Serializer
from rest_framework.fields import (
    CharField,
    IntegerField,
    ListField,
    SerializerMethodField,
)

from lessons.utils.serializer_utils import get_n, StudentNDefault
from .given import get_matrix_a


class TaskGivenSerializer(Serializer):
    text = CharField()
    matrix_a = SerializerMethodField()

    def get_matrix_a(self, _) -> List[List[int]]:
        n = get_n(self.context['request'])
        return get_matrix_a(n)


class TaskResultSerializer(Serializer):
    n = IntegerField(default=StudentNDefault())
    product = ListField(child=ListField(child=IntegerField()))
    trace = IntegerField()
