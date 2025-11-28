from django.contrib import admin
from django.urls import path
from Mutiapp import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("a/", views.index_view, name="home"),

    # Correct mapping
    path("mov/", views.movies_view, name="movies"),
    path("spo/", views.sports_view, name="sports"),
    path("pol/", views.politics_view, name="politics"),
]
