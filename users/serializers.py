from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField,
    DateTimeField,
    SerializerMethodField,
)
from rest_auth.models import TokenModel

from .models import (
    Profile,
    Group,
)


class TokenSerializer(ModelSerializer):
    class Meta:
        model = TokenModel
        fields = ['token']

    token = CharField(source='key', max_length=40)


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'email', 'type',
                  'date_joined', 'dark_mode']

    id = CharField(source='user.id', read_only=True)
    first_name = CharField(source='user.first_name', read_only=True)
    last_name = CharField(source='user.last_name', read_only=True)
    email = EmailField(source='user.email', read_only=True)
    date_joined = DateTimeField(source='user.date_joined', read_only=True)
    type = SerializerMethodField()

    def get_type(self, profile):
        user = profile.user
        if user.is_superuser:
            return 'admin'
        if user.is_staff:
            return 'teacher'
        return 'student'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']
