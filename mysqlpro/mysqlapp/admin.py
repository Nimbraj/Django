from django.contrib import admin

# Register your models here.
from .models import Employee
class EmpAdmin(models.ModelAdmin):
    list_dispaly=['id','name,','salary','age','email','doj']
admin.site.register(Employee,EmpAdmin)