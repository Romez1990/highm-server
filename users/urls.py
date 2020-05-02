from django.urls import path, include
from rest_auth.views import LoginView, LogoutView

from highm_server.settings import DEBUG
from .views import (
    ProfileView,
)

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
]

if DEBUG:
    urlpatterns += [
        path('session-auth/', include('rest_framework.urls')),
    ]
