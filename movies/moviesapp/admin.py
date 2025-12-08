from django.contrib import admin
from .models import Moviesed

class Moviese(admin.ModelAdmin):
    list_display = ['id', 'name_movies', 'date_reliz', 'hiro_name', 'hiroen_name', 'name_aother']

admin.site.register(Moviesed, Moviese)
