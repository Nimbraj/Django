from django.contrib import admin
from .models import modelform
class ModelFrom(admin.ModelAdmin):
    list_display=['id','name','age','marks','email']
    # Register your models here.
admin.site.register(modelform,ModelFrom)