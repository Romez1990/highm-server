from typing import List
from rest_framework.serializers import Serializer


class TaskBase:
    result_serializer: Serializer
    given_serializer: Serializer
    text: str = 'None'
    steps: List = []

    def check(self):
        for index, step in enumerate(self.steps):
            result = step.check(self)
            if not result:
                return index
        return True
