from django.contrib import admin
from django.urls import path,include
from reminders.views import create_reminder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reminders.urls')), 
]
