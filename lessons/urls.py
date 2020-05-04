from rest_framework.routers import SimpleRouter

from .views import (
    LessonViewSet,
)

router = SimpleRouter()
router.register('lesson', LessonViewSet, basename='lesson')
urlpatterns = router.urls
