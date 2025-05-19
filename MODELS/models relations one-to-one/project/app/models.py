from django.db import models

# Create your models here.
class Adhar(models.Model):
    adhar=models.IntegerField(unique=True)
    created_by=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.adhar)
    
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    contact=models.IntegerField()
    aadhar=models.OneToOneField(Adhar,on_delete=models.PROTECT,to_field="adhar")


