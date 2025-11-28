from django.db import models


# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.IntegerField()
    email=models.EmailField(max_length=254)
    doj=models.DateField()