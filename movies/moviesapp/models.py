from django.db import models

# Create your models here.
class Moviesed(models.Model):
    name_movies=models.CharField( max_length=50)
    date_reliz=models.DateField(auto_now=False, auto_now_add=False)
    hiro_name=models.CharField(max_length=50)
    hiroen_name=models.CharField(max_length=50)
    name_aother=models.CharField(max_length=50)
    
    