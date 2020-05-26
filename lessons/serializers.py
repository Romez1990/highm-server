from rest_framework.serializers import (
    ModelSerializer,
)

from users.serializers import (
    StudentBasicSerializer,
)
from .models import (
    TaskResult,
    LessonResult,
)


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
        fields = ['grade', 'task_results']

    task_results = TaskResultForStudentSerializer(many=True)


class LessonResultForStatementSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['id', 'student', 'grade']

    student = StudentBasicSerializer()


class LessonResultForStatementAnswersSerializer(ModelSerializer):
    class Meta:
        model = LessonResult
        fields = ['task_results']

    task_results = TaskResultForStatementSerializer(many=True)
