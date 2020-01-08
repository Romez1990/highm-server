from django.db.models import (
    Model,
    CharField,
    DateTimeField,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(Model):
    name = CharField(verbose_name='Name', max_length=30, unique=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
