from django.urls import path, include
from rest_framework.routers import DefaultRouter

from highm_server.settings import DEBUG
from .views import (
    ProfileView,
    GroupViewSet,
    RegistrationCodeViewSet,
    RegisterView,
    VerifyEmailView,
)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('accounts/', include('allauth.urls')),
]

if DEBUG:
    urlpatterns += [
        path('session-auth/', include('rest_framework.urls')),
    ]

router = DefaultRouter()
router.register('auth/registration-code', RegistrationCodeViewSet,
                basename='registration-code')
router.register('group', GroupViewSet, basename='group')
urlpatterns += router.urls
