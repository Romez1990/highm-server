from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    lesson_list,
    lesson_retrieve,
    lesson_check,
)

urlpatterns = [
    path('lesson/', lesson_list),
    path('lesson/<int:lesson_pk>/', lesson_retrieve),
    path('lesson/<int:lesson_pk>/check/', lesson_check),
]