from random import randint
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


def user_display(user) -> str:
    return f'{user.first_name} {user.last_name}'


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


class UnregisteredUser(Model):
    code = CharField(verbose_name='Code', max_length=7, primary_key=True,
                     unique=True)
    first_name = CharField(verbose_name='First name', max_length=50)
    last_name = CharField(verbose_name='Last name', max_length=50)
    group = ForeignKey(Group, verbose_name='Group',
                       related_name='unregistered_students', on_delete=PROTECT,
                       null=True)
    is_staff = BooleanField('Is staff')
    created_at = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.generate_code()
        super().save(*args, **kwargs)

    def generate_code(self):
        while True:
            code = f'c{str(randint(0, 999_999)).zfill(6)}'
            if not UnregisteredUser.objects.filter(code=code).exists():
                break
        self.code = code

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.code}'
