from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    LessonViewSet,
    StatementListView,
    StatementDetailView,
)

lesson_router = SimpleRouter()
lesson_router.register('lesson', LessonViewSet, basename='lesson')

urlpatterns = [
    path('', include(lesson_router.urls)),
    path('statement/group/<str:group>/lesson/<int:lesson>/',
         StatementListView.as_view(), name='statement-list'),
    path('statement/group/<str:group>/lesson/<int:lesson>/<int:pk>/',
         StatementDetailView.as_view(), name='statement-detail'),
]
