from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_auth.views import LoginView, LogoutView

from highm_server.settings import DEBUG
from .views import (
    ProfileView,
    StudentViewSet,
    TeacherViewSet,
    GroupViewSet,
)

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
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
