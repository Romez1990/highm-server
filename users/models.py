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
        if self.user.is_superuser:
            return 1

        users = self.group.students.values_list('user__first_name',
                                                'user__last_name')
        unregistered_users = self.group.unregistered_students.values_list(
            'first_name', 'last_name')
        # it's already ordered
        all_users = users.union(unregistered_users)
        for number, (first_name, last_name) in enumerate(all_users, 1):
            if last_name == self.user.last_name and \
                    first_name == self.user.first_name:
                return number

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Teacher(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class UnregisteredUser(Model):
    registration_code = CharField(verbose_name='Code', max_length=7,
                                  primary_key=True, unique=True)
    first_name = CharField(verbose_name='First name', max_length=50)
    last_name = CharField(verbose_name='Last name', max_length=50)
    group = ForeignKey(Group, verbose_name='Group',
                       related_name='unregistered_students', on_delete=PROTECT,
                       null=True)
    is_staff = BooleanField('Is staff')
    created_at = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.registration_code:
            self.generate_code()
        super().save(*args, **kwargs)

    def generate_code(self):
        while True:
            registration_code = f'c{str(randint(0, 999_999)).zfill(6)}'
            queryset = UnregisteredUser.objects.filter(
                registration_code=registration_code)
            if not queryset.exists():
                break
        self.registration_code = registration_code

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.registration_code}'
