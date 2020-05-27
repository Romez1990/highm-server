from django.urls import path, include
from rest_framework.routers import SimpleRouter

from highm_server.custom_lookup_type_router import CustomLookupTypeRouter
from .views_for_student import (
    LessonViewSet,
)
from .views_for_teacher import (
    TeacherLessonViewSet,
    LessonResultViewSet,
)

router = CustomLookupTypeRouter()
router.register('lesson', LessonViewSet, basename='lesson')

teacher_lesson_router = SimpleRouter()
teacher_lesson_router.register('lesson', TeacherLessonViewSet,
                               basename='teacher-lesson')

statement_router = SimpleRouter()
statement_router.register('result', LessonResultViewSet,
                          basename='lesson-result')

urlpatterns = [
    path('', include(router.urls)),
    path('teacher-panel/group/<str:group>/',
         include(teacher_lesson_router.urls)),
    path('teacher-panel/group/<str:group>/lesson/<int:lesson>/',
         include(statement_router.urls)),
]
