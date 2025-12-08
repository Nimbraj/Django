from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    marks = models.CharField(max_length=20)
    password = models.CharField(max_length=234)
    feedback = models.CharField(max_length=100)

    def __str__(self):
        return self.name
