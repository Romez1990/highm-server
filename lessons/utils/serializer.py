from rest_framework.fields import ListField, Field


class MatrixField:
    def __new__(cls, *, child: Field) -> object:
        return ListField(child=ListField(child=child))
