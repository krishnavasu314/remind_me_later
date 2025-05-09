from django.urls import path
from .views import create_reminder

urlpatterns = [
    path('reminders/', create_reminder),
]
