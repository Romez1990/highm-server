from django.db.models import (
    Model,
    CharField,
    BooleanField,
    DateTimeField,
    OneToOneField,
    CASCADE,
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
