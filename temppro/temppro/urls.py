from django.contrib import admin
from django.urls import path
from tempapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("first/", views.firstTemplate),
]
