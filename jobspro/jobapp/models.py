from django.db import models

class Punejob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    salary = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()

class Bangjob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    salary = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()

class Bhiharjob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    salary = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
