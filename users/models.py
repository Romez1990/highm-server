from django.db.models import (
    Model,
    CharField,
    BooleanField,
    DateTimeField,
    OneToOneField,
    ForeignKey,
    CASCADE,
    PROTECT,
)
from django.contrib.auth import get_user_model

from users.validators import group_name_validator

User = get_user_model()


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    dark_mode = BooleanField(verbose_name='Dark mode', default=False)

    def __str__(self):
        return f'{self.user.username} {self.user.first_name} ' \
               f'{self.user.last_name}'


GROUP_ADMINS = 'admins'


class Group(Model):
    name = CharField(verbose_name='Name', max_length=30, unique=True,
                     validators=[group_name_validator])
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    group = ForeignKey(Group, verbose_name='Group', related_name='students',
                       on_delete=PROTECT)

    @property
    def n(self):
        students = self.group.students.order_by('user__first_name',
                                                'user__last_name')
        for index, student in enumerate(students):
            if student == self:
                return index + 1
        raise ValueError('Student must be found')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Teacher(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
