from django.urls import path
from accounts.views import Registration

app_name = 'accounts'

urlpatterns = [
    path('register/', Registration.as_view(), name='register'),
]