from django.urls import path, include

from highm_server.settings import DEBUG
from .views import (
    ProfileView,
)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
]

if DEBUG:
    urlpatterns += [
        path('session-auth/', include('rest_framework.urls')),
    ]
