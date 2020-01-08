from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    GroupViewSet,
)

urlpatterns = [
]

router = DefaultRouter()
router.register('group', GroupViewSet, basename='group')
urlpatterns += router.urls
