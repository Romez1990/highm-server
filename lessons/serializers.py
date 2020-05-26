from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
)

from users.serializers import (
    StudentBasicSerializer,
)
from .models import (
    TaskResult,
    LessonResult,
)


class LessonForTeacherSerializer(Serializer):
    title = CharField(max_length=150)


class TaskResultForStudentSerializer(ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ['task_number', 'correct']


class TaskResultForStatementSerializer(ModelSerializer):
    class Meta:
        model = TaskResult
        fields = ['task_number', 'correct', 'answer']


class LessonResultForStudentSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['grade', 'percent_correct', 'task_results']

    task_results = TaskResultForStudentSerializer(many=True)


class LessonResultForStatementSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['id', 'student', 'n', 'percent_correct', 'grade']

    student = StudentBasicSerializer()


class LessonResultForStatementAnswersSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['task_results']

    task_results = TaskResultForStatementSerializer(many=True)
