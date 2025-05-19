from django.db import models

# Create your models here.
class workers(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    discrip=models.CharField(max_length=300)
    phone=models.IntegerField(max_length=50)
    dob=models.DateField(max_length=50)
    subscribe=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image/')
    resume=models.FileField(upload_to='file/')
    password=models.CharField(max_length=50)

