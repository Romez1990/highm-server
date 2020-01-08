from django.urls import path, include
from rest_framework.routers import DefaultRouter

from highm_server.settings import DEBUG
from .views import (
    ProfileView,
    GroupViewSet,
)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
]

if DEBUG:
    urlpatterns += [
        path('session-auth/', include('rest_framework.urls')),
    ]

router = DefaultRouter()
router.register('group', GroupViewSet, basename='group')
urlpatterns += router.urls
