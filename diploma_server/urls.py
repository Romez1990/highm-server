from django.contrib import admin
from django.urls import path, include
from djoser.views import TokenCreateView, TokenDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/login/', TokenCreateView.as_view(), name='login'),
    path('api/logout/', TokenDestroyView.as_view(), name='logout'),
]
