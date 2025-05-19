from django.db import models

# Create your models here.
class Baseinfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)

class Student(Baseinfo):
    rollno=models.IntegerField(max_length=50)
    branch=models.CharField(max_length=50)

class Employ(Baseinfo):
    salary=models.IntegerField(max_length=60)
    age=models.IntegerField(max_length=60)