from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    IntegerField,
)
from django.contrib.postgres.fields import (
    JSONField,
)

from users.models import (
    Student,
)


class LessonResult(Model):
    student = ForeignKey(Student, CASCADE)
    n = IntegerField()
    lesson_number = IntegerField()
    grade = IntegerField()

    @property
    def points(self) -> int:
        return sum(task_result.points
                   for task_result in self.task_results.all())

    @property
    def max_points(self) -> int:
        from lessons.lessons import Lessons
        number = self.lesson_number
        return Lessons.lesson_max_points(number)

    class Meta:
        unique_together = ['student', 'lesson_number']


class TaskResult(Model):
    lesson_result = ForeignKey(LessonResult, CASCADE,
                               related_name='task_results')
    task_number = IntegerField()
    points = IntegerField()
    answer = JSONField()

    @property
    def max_points(self) -> int:
        from lessons.lessons import Lessons
        lesson_number = self.lesson_result.lesson_number
        number = self.task_number
        return Lessons.task_max_points(lesson_number, number)

    class Meta:
        unique_together = ['lesson_result', 'task_number']
