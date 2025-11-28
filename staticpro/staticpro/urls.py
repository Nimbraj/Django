from django.contrib import admin
from django.urls import path
from staticapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("state/", views.staticdata),   # corrected URL
]
