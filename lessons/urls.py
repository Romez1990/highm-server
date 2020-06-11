from django.urls import path, include
from rest_framework.routers import SimpleRouter

from highm_server.custom_lookup_type_router import CustomLookupTypeRouter
from .views_for_student import (
    LessonViewSet,
)
from .views_for_teacher import (
    TeacherLessonViewSet,
    GroupStatementViewSet,
    LessonResultViewSet,
)

root_router = CustomLookupTypeRouter()
root_router.register('lesson', LessonViewSet, basename='lesson')

group_router = SimpleRouter()
group_router.register('lesson', TeacherLessonViewSet,
                      basename='teacher-lesson')
group_router.register('statement', GroupStatementViewSet,
                      basename='group-statement')

lesson_router = SimpleRouter()
lesson_router.register('result', LessonResultViewSet,
                       basename='lesson-result')

urlpatterns = [
    path('', include(root_router.urls)),
    path('teacher-panel/group/<str:group>/', include(group_router.urls)),
    path('teacher-panel/group/<str:group>/lesson/<int:lesson>/',
         include(lesson_router.urls)),
]
