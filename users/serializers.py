from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    EmailField,
    SerializerMethodField,
    ValidationError,
)
from rest_auth.models import TokenModel
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import email_address_exists
from allauth.account import app_settings as allauth_settings

from .models import (
    User,
    Profile,
    Group,
    Student,
    RegistrationCode,
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


class RegistrationCodeSerializer(ModelSerializer):
    class Meta:
        model = RegistrationCode
        fields = ['code', 'first_name', 'last_name']
        read_only_fields = ['code']

    def create(self, validated_data):
        registration_code = RegistrationCode(**validated_data)
        registration_code.generate_code()
        registration_code.save()
        return registration_code


class RegistrationUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']


class RegisterSerializer(Serializer):
    registration_code = CharField(min_length=6, max_length=6)
    user = RegistrationUserSerializer()

    def validate_registration_code(self, registration_code):
        try:
            registration_code_object = RegistrationCode.objects.get(
                pk=registration_code)
        except RegistrationCode.DoesNotExist:
            raise ValidationError({
                'registration_code': 'wrong registration code'
            })
        return registration_code_object

    def validate_user(self, user):
        user.username = get_adapter().clean_username(user['email'])
        user.email = get_adapter().clean_email(user['email'])
        if allauth_settings.UNIQUE_EMAIL:
            if user.email and email_address_exists(user['email']):
                raise ValidationError(
                    'A user is already registered with this email address.')
        user.password = get_adapter().clean_password(user['password'])
        return user

    def custom_signup(self, request, user):
        registration_code = self.validated_data['registration_code']
        user.first_name = registration_code.first_name
        user.last_name = registration_code.last_name
        user.save()
        Profile.objects.create(user=user)
        Student.objects.create(user=user, group=registration_code.group)
        registration_code.delete()

    def get_cleaned_data(self):
        return {
            'username': self.validated_data['user']['email'],
            'email': self.validated_data['user']['email'],
            'password': self.validated_data['user']['password'],
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

    def create(self, validated_data):
        raise NotImplemented('cannot create registration')

    def update(self, instance, validated_data):
        raise NotImplemented('cannot update registration')
