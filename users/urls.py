from django.urls import path, include
from rest_framework.routers import SimpleRouter

from highm_server.settings import DEBUG
from .views import (
    ProfileView,
    StudentViewSet,
    GroupViewSet,
)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
]

router = SimpleRouter()
router.register('student', StudentViewSet, basename='student')
router.register('group', GroupViewSet, basename='group')
urlpatterns += router.urls

if DEBUG:
    urlpatterns += [
        path('session-auth/', include('rest_framework.urls')),
    ]
