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
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import email_address_exists
from allauth.account import app_settings as allauth_settings

from .models import (
    Profile,
    Group,
    Student,
    Teacher,
    UnregisteredUser,
)
from .validators import registration_code_validator


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


class TeacherSerializer(ModelSerializer, UserSerializerMixin):
    class Meta:
        model = Teacher
        fields = UserSerializerMixin.Meta.fields + []

    def update(self, instance, validated_data):
        UserSerializerMixin.update(self, instance.user,
                                   validated_data.pop('user', {}))
        return instance


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


class RegisterSerializer(Serializer):
    registration_code = CharField(min_length=7, max_length=7,
                                  validators=[registration_code_validator])
    first_name = CharField(max_length=254)
    last_name = CharField(max_length=254)
    email = EmailField(max_length=254)
    password = CharField(max_length=128)

    def validate_registration_code(self, registration_code):
        try:
            registration_code_object = UnregisteredUser.objects.get(
                pk=registration_code)
        except UnregisteredUser.DoesNotExist:
            raise ValidationError(['Wrong registration code.'])
        return registration_code_object

    def validate_email(self, email):
        clean_email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL and email_address_exists(clean_email):
            raise ValidationError({
                'email': [
                    'A user is already registered with this email address.'
                ]
            })
        return clean_email

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    def validate(self, attrs):
        registration_code = attrs['registration_code']
        first_name = attrs['first_name']
        last_name = attrs['last_name']
        if registration_code.first_name != first_name or \
                registration_code.last_name != last_name:
            raise ValidationError({
                'names': [
                    'Wrong first name or last name.'
                ]
            })
        return attrs

    def get_cleaned_data(self):
        return {
            'username': self.validated_data['email'],
            'email': self.validated_data['email'],
            'password': self.validated_data['password'],
        }

    def custom_signup(self, request, user):
        registration_code = self.validated_data['registration_code']
        user.first_name = registration_code.first_name
        user.last_name = registration_code.last_name
        user.save()
        Profile.objects.create(user=user)
        Student.objects.create(user=user, group=registration_code.group)
        registration_code.delete()

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
