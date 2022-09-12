from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('drf_social_oauth2.urls')),
    path('api/', include('accounts.urls')),
]
