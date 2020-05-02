from django.db.models import (
    Model,
    BooleanField,
    OneToOneField,
    CASCADE,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    dark_mode = BooleanField(verbose_name='Dark mode', default=False)

    def __str__(self):
        return f'{self.user.username} {self.user.first_name} ' \
               f'{self.user.last_name}'
