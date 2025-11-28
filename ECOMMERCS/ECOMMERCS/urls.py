"""
URL configuration for ECOMMERCS project.
"""

from django.contrib import admin
from django.urls import path
from secapp import views   # ✅ Replace `myapp` with the actual name of your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', views.Greet, name='greet'),
    path('time/', views.time, name='time'),
]












