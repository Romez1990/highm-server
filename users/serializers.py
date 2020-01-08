from rest_framework.serializers import (
    ModelSerializer,
    CharField,
)
from rest_auth.models import TokenModel


class TokenSerializer(ModelSerializer):
    class Meta:
        model = TokenModel
        fields = ['token']

    token = CharField(source='key', max_length=40)
