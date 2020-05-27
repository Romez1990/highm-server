from django.urls import path, include

from highm_server.custom_lookup_type_router import CustomLookupTypeRouter
from .views_for_student import (
    LessonViewSet,
)

router = CustomLookupTypeRouter()
router.register('lesson', LessonViewSet, basename='lesson')

urlpatterns = [
    path('', include(router.urls)),
]
