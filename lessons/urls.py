from django.urls import path

from .views import (
    lesson_list,
    lesson_retrieve,
    lesson_check,
)

urlpatterns = [
    path('lesson/', lesson_list),
    path('lesson/<int:number>/', lesson_retrieve),
    path('lesson/<int:number>/check/', lesson_check),
]
