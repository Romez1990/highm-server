from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_auth.views import LoginView, LogoutView
from rest_auth.registration.views import RegisterView

from highm_server.settings import DEBUG
from .views import (
    ProfileView,
    StudentViewSet,
    TeacherViewSet,
    GroupViewSet,
    RegistrationCodeCheckView,
    EmailVerificationKeyCheckView,
    VerifyEmailView,
)

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/registration-code-check/', RegistrationCodeCheckView.as_view(),
         name='registration_code_check'),
    path('auth/verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('auth/email-verification-key-check/',
         EmailVerificationKeyCheckView.as_view(),
         name='email_verification_key_check'),
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
