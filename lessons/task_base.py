from typing import List
from rest_framework.serializers import Serializer


class TaskBase:
    result_serializer: Serializer
    given_serializer: Serializer
    text: str = 'None'
    steps: List = []

    def check(self) -> bool:
        return all([step.check(self) for step in self.steps])
