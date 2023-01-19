from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=100,primary_key=True)    
    def __str__(self):
        return self.name

    
    
class Student(models.Model):
    name=models.ForeignKey(School,on_delete=models.CASCADE)
    sname=models.CharField(max_length=100)
    email=models.EmailField()
    
    def __str__(self):
        return self.sname
