from rest_framework.generics import (
    RetrieveUpdateAPIView,
)

from .models import (
    Profile,
)
from .serializers import (
    ProfileSerializer,
)
from .permissions import (
    IsAuthenticated,
)


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def get_queryset(self):
        return Profile.objects.none()
