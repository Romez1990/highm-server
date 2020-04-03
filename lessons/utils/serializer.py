from rest_framework.serializers import Serializer
from rest_framework.fields import IntegerField, ListField, Field


def get_n(serializer: Serializer) -> int:
    request = serializer.context['request']
    return request.user.student.n


class StudentNDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return get_n(serializer_field)


class StudentNField:
    def __new__(cls) -> IntegerField:
        return IntegerField(default=StudentNDefault())


class MatrixField:
    def __new__(cls, *, child: Field) -> object:
        return ListField(child=ListField(child=child))
