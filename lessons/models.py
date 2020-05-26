from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    IntegerField,
    FloatField,
    BooleanField,
)
from django.contrib.postgres.fields import (
    JSONField,
)

from users.models import (
    Student,
)


class LessonResult(Model):
    student = ForeignKey(Student, CASCADE)
    lesson_number = IntegerField()
    grade = FloatField()

    class Meta:
        unique_together = ['student', 'lesson_number']


class TaskResult(Model):
    lesson_result = ForeignKey(LessonResult, CASCADE,
                               related_name='task_results')
    task_number = IntegerField()
    correct = BooleanField()
    answer = JSONField()

    class Meta:
        unique_together = ['lesson_result', 'task_number']
