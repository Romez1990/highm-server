from django.urls import path, include

from highm_server.settings import DEBUG

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
]

if DEBUG:
    urlpatterns += [
        path('session-auth/', include('rest_framework.urls')),
    ]
