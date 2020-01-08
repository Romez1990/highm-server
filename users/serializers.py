from rest_framework.serializers import (
    ModelSerializer,
)

from .models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

    def get_number_of_students(self, group):
        return group.students.count() + group.unregistered_students.count()
