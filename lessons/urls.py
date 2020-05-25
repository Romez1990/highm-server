from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    LessonViewSet,
    StatementListView,
    StatementDetailView,
)

urlpatterns = [
    path('statement/group/<str:group>/lesson/<int:lesson>/',
         StatementListView.as_view(), name='statement-list'),
    path('statement/group/<str:group>/lesson/<int:lesson>/<int:pk>/',
         StatementDetailView.as_view(), name='statement-detail'),
]

router = SimpleRouter()
router.register('lesson', LessonViewSet, basename='lesson')
urlpatterns += router.urls
