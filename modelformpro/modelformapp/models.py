from django.db import models

class modelform(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
