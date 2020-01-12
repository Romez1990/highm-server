from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    IntegerField,
    CharField,
    EmailField,
    DateTimeField,
    SerializerMethodField,
)
from rest_framework.exceptions import ValidationError
from rest_auth.models import TokenModel

from .models import (
    Profile,
    Group,
    Student,
)


class UserSerializerMixin(Serializer):
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined']

    id = IntegerField(source='user.id', read_only=True)
    first_name = CharField(source='user.first_name')
    last_name = CharField(source='user.last_name')
    email = EmailField(source='user.email', read_only=True)
    date_joined = DateTimeField(source='user.date_joined', read_only=True)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()


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


class StudentSerializer(ModelSerializer, UserSerializerMixin):
    class Meta:
        model = Student
        fields = UserSerializerMixin.Meta.fields + ['group_name']

    group_name = CharField(source='group.name')

    def update(self, instance, validated_data):
        UserSerializerMixin.update(self, instance.user,
                                   validated_data.pop('user', {}))
        group_name = validated_data.pop('group', {}).pop('name', None)
        self.set_group(instance, group_name)
        instance.save()
        return instance

    def set_group(self, instance, group_name):
        if group_name is None:
            return
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            raise ValidationError({
                'group_name': ['Group not found.']
            })
        instance.group = group


class GroupBasicSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'number_of_students']

    number_of_students = SerializerMethodField(read_only=True)

    def get_number_of_students(self, group):
        return group.students.count()


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'students']

    students = StudentSerializer(many=True)
