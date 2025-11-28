from django.db import models

# Create your models here.
class Employee(models.Model):
    # The primary key is often created automatically, 
    # but if you want to explicitly define an ID:
    eid = models.IntegerField(unique=True) # Assuming 'eid' should be unique
    
    # Correct field type is CharField, not Varchar
    ename = models.CharField(max_length=100) # CharField requires a max_length argument

    def __str__(self):
        return self.ename