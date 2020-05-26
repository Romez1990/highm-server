from django.urls import path, include
from rest_framework.routers import SimpleRouter

from highm_server.custom_lookup_type_router import CustomLookupTypeRouter
from .views import (
    LessonViewSet,
    LessonForTeacherViewSet,
    StatementViewSet,
)

lesson_router = CustomLookupTypeRouter()
lesson_router.register('lesson', LessonViewSet, basename='lesson')

teacher_lesson_router = SimpleRouter()
teacher_lesson_router.register('lesson', LessonForTeacherViewSet,
                               basename='teacher-lesson')

statement_router = SimpleRouter()
statement_router.register('statement', StatementViewSet, basename='statement')

urlpatterns = [
    path('', include(lesson_router.urls)),
    path('teacher-panel/group/<str:group>/',
         include(teacher_lesson_router.urls)),
    path('teacher-panel/group/<str:group>/lesson/<int:lesson>/',
         include(statement_router.urls)),
]
