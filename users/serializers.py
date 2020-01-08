from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    EmailField,
    SerializerMethodField,
)
from rest_auth.models import TokenModel

from .models import (
    Profile,
    Group,
)


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'type', 'group',
                  'dark_mode']
        read_only_fields = []

    first_name = CharField(source='user.first_name', read_only=True)
    last_name = CharField(source='user.last_name', read_only=True)
    email = EmailField(source='user.email', read_only=True)
    type = SerializerMethodField()
    group = CharField(source='user.student.group.name', read_only=True)

    def get_type(self, obj):
        user = obj.user
        return 'admin' if user.is_superuser else \
            'teacher' if user.is_staff else \
            'student'


class TokenSerializer(ModelSerializer):
    class Meta:
        model = TokenModel
        fields = ['token']

    token = CharField(source='key', max_length=40)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

    def get_number_of_students(self, group):
        return group.students.count() + group.unregistered_students.count()
