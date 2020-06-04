from django.db.models import Model

from users.models import (
    User,
    Teacher,
    Student,
)


class DefaultField:
    requires_context = True

    def __call__(self, serializer_field):
        request = serializer_field.context['request']
        user = request.user
        return self._get_default(user)

    def _get_default(self, user: User) -> Model:
        raise NotImplementedError


class CurrentTeacherDefault(DefaultField):
    def _get_default(self, user: User) -> Teacher:
        return user.teacher


class CurrentStudentDefault(DefaultField):
    def _get_default(self, user: User) -> Student:
        return user.student
