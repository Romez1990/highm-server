from django.core.validators import RegexValidator
from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    IntegerField,
    CharField,
    EmailField,
    DateTimeField,
    ListField,
    SerializerMethodField,
    HiddenField,
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
    GROUP_ADMINS,
    Student,
    Teacher,
    UnregisteredUser,
)
from .fields import CurrentTeacherDefault


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


class StudentBasicSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']

    first_name = CharField(source='user.first_name', read_only=True)
    last_name = CharField(source='user.last_name', read_only=True)


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

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['registered'] = True
        return ret


class TeacherSerializer(ModelSerializer, UserSerializerMixin):
    class Meta:
        model = Teacher
        fields = UserSerializerMixin.Meta.fields + []

    def update(self, instance, validated_data):
        UserSerializerMixin.update(self, instance.user,
                                   validated_data.pop('user', {}))
        return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['registered'] = True
        return ret


class UnregisteredUserBasicSerializer(ModelSerializer):
    class Meta:
        model = UnregisteredUser
        fields = ['registration_code', 'first_name', 'last_name']
        read_only_fields = ['registration_code']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['registered'] = False
        return ret


class UnregisteredStudentSerializer(ModelSerializer):
    class Meta:
        model = UnregisteredUser
        fields = ['registration_code', 'first_name', 'last_name', 'group_name']
        read_only_fields = ['registration_code']

    group_name = CharField(source='group.name')

    def create(self, validated_data):
        validated_data['is_staff'] = False
        group_name = validated_data.pop('group', {}).pop('name', None)
        validated_data['group'] = self.get_group(group_name)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        group_name = validated_data.pop('group', {}).pop('name', None)
        instance.group = self.get_group(group_name)
        return super().update(instance, validated_data)

    def get_group(self, group_name):
        if group_name is None:
            return None
        user = self.context['request'].user
        try:
            queryset = Group.objects
            if user.is_superuser:
                return queryset.get(name=group_name)
            return queryset.exclude(name=GROUP_ADMINS).get(name=group_name)
        except Group.DoesNotExist:
            raise ValidationError({
                'group_name': ['Group not found.']
            })

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['registered'] = False
        return ret


class UnregisteredTeacherCreateSerializer(ModelSerializer):
    class Meta:
        model = UnregisteredUser
        fields = ['registration_code', 'first_name', 'last_name']
        read_only_fields = ['registration_code']

    def create(self, validated_data):
        validated_data['is_staff'] = True
        return super().create(validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['registered'] = False
        return ret


class GroupBasicSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'number_of_students']

    number_of_students = SerializerMethodField(read_only=True)

    def get_number_of_students(self, group):
        return group.students.count() + group.unregistered_students.count()


class GroupCreateSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['teacher', 'name', 'students']

    teacher = HiddenField(default=CurrentTeacherDefault())
    students = ListField(
        child=UnregisteredUserBasicSerializer(), max_length=50,
        required=False)

    def create(self, validated_data):
        group = super().create({
            'teacher': validated_data['teacher'],
            'name': validated_data['name'],
        })
        if 'students' in validated_data:
            UnregisteredUser.objects.bulk_create([
                UnregisteredUser(**registration_code, group=group,
                                 is_staff=False).generate_code()
                for registration_code in validated_data['students']
            ])
        return validated_data


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'students']

    students = SerializerMethodField()

    def get_students(self, group):
        registered = StudentSerializer(group.students, many=True).data
        unregistered = UnregisteredUserBasicSerializer(
            group.unregistered_students, many=True).data
        return registered + unregistered


registration_code_validator = RegexValidator(r'^c\d{6}$',
                                             'Wrong registration code.')


class RegistrationCodeCheckSerializer(Serializer):
    registration_code = CharField(min_length=7, max_length=7,
                                  validators=[registration_code_validator])
    first_name = CharField(max_length=254)
    last_name = CharField(max_length=254)

    def validate_registration_code(self, registration_code):
        try:
            registration_code_object = UnregisteredUser.objects.get(
                pk=registration_code)
        except UnregisteredUser.DoesNotExist:
            raise ValidationError(['Wrong registration code.'])
        return registration_code_object

    def validate(self, attrs):
        registration_code = attrs['registration_code']
        first_name = attrs['first_name']
        last_name = attrs['last_name']
        if registration_code.first_name != first_name or \
                registration_code.last_name != last_name:
            raise ValidationError({
                'names': [
                    'Names do not match names from registration code.'
                ]
            })
        return attrs


class RegisterSerializer(RegistrationCodeCheckSerializer):
    email = EmailField(max_length=254)
    password = CharField(max_length=128)

    def validate_email(self, email):
        clean_email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL and email_address_exists(clean_email):
            raise ValidationError([
                'A user is already registered with this email address.'
            ])
        return clean_email

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    def get_cleaned_data(self):
        return {
            'unregistered_user': self.validated_data['registration_code'],
            'first_name': self.validated_data['first_name'],
            'last_name': self.validated_data['last_name'],
            'email': self.validated_data['email'],
            'password': self.validated_data['password'],
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user
