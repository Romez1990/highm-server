from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_auth.registration.views import RegisterView

from highm_server.settings import DEBUG
from .views import (
    ProfileView,
    StudentViewSet,
    TeacherViewSet,
    GroupViewSet,
    VerifyEmailView,
)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('accounts/', include('allauth.urls')),
]

router = SimpleRouter()
router.register('student', StudentViewSet, basename='student')
router.register('teacher', TeacherViewSet, basename='teacher')
router.register('group', GroupViewSet, basename='group')
urlpatterns += router.urls

if DEBUG:
    urlpatterns += [
        path('session-auth/', include('rest_framework.urls')),
    ]
