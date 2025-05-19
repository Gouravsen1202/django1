from django.db import models

# Create your models here.
class Baseinfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    contact=models.IntegerField()

class Student(Baseinfo):
    branch=models.CharField(max_length=50)
    fees=models.IntegerField()

class Employ(Baseinfo):
    department=models.CharField(max_length=50)
    salary=models.IntegerField()




