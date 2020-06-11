from typing import (
    Optional,
    List,
)

from django.db.models import QuerySet
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    IntegerField,
    SerializerMethodField,
)

from users.models import (
    Student,
    UnregisteredUser,
    Group,
)
from .lessons import LessonsForTeacher
from .models import (
    TaskResult,
    LessonResult,
)


class LessonBasicSerializer(Serializer):
    title = CharField(max_length=150)


class GroupStatementStudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'grades']

    id = IntegerField(source='user.id', read_only=True)
    first_name = CharField(source='user.first_name')
    last_name = CharField(source='user.last_name')
    grades = SerializerMethodField()

    def get_grades(self, student: Student) -> List[Optional[int]]:
        number_of_lessons = LessonsForTeacher.number_of_lessons() + 1
        return [self._get_grade(student.lesson_results, number)
                for number in range(1, number_of_lessons)]

    def _get_grade(self, results: QuerySet, number: int) -> Optional[int]:
        result: LessonResult = results.filter(lesson_number=number).first()
        if result is None:
            return None
        return result.grade

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['registered'] = True
        return ret


class GroupStatementUnregisteredStudentSerializer(ModelSerializer):
    class Meta:
        model = UnregisteredUser
        fields = ['registration_code', 'first_name', 'last_name']
        read_only_fields = ['registration_code']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['registered'] = False
        return ret


class GroupStatementSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['students']

    students = SerializerMethodField()

    def get_students(self, group: Group):
        registered = GroupStatementStudentSerializer(group.students,
                                                     many=True).data
        unregistered = GroupStatementUnregisteredStudentSerializer(
            group.unregistered_students, many=True).data
        return registered + unregistered


class LessonResultSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['id', 'student_id', 'n', 'grade', 'points', 'max_points']

    max_points = IntegerField()


class TaskResultSerializer(ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ['points', 'max_points', 'answer']


class LessonResultAnswersSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['task_results']

    task_results = TaskResultSerializer(many=True)
