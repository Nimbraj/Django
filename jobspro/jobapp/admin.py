from django.contrib import admin
from django.contrib import admin
from .models import Punejob, Bangjob, Bhiharjob

@admin.register(Punejob)
class PunejobAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'company', 'title', 'address', 'salary', 'email', 'phone')
    search_fields = ('company', 'title')
    list_filter = ('date', 'company')


@admin.register(Bangjob)
class BangjobAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'company', 'title', 'address', 'salary', 'email', 'phone')
    search_fields = ('company', 'title')
    list_filter = ('date', 'company')


@admin.register(Bhiharjob)
class BhiharjobAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'company', 'title', 'address', 'salary', 'email', 'phone')
    search_fields = ('company', 'title')
    list_filter = ('date', 'company')
  
# Register your models here.
