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

User = get_user_model()


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    dark_mode = BooleanField(verbose_name='Dark mode', default=False)

    def __str__(self):
        return f'{self.user.username} {self.user.first_name} ' \
               f'{self.user.last_name}'


class Group(Model):
    name = CharField(verbose_name='Name', max_length=30, unique=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    group = ForeignKey(Group, verbose_name='Group', related_name='students',
                       on_delete=PROTECT)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class RegistrationCode(Model):
    code = CharField(verbose_name='Code', max_length=6, primary_key=True)
    first_name = CharField(verbose_name='First name', max_length=50)
    last_name = CharField(verbose_name='Last name', max_length=50)
    group = ForeignKey(Group, verbose_name='Group',
                       related_name='unregistered_students', on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True)

    def generate_code(self):
        while True:
            code = str(randint(0, 999_999)).zfill(6)
            if RegistrationCode.objects.filter(code=code).count() == 0:
                break
        self.code = code

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.code}'
