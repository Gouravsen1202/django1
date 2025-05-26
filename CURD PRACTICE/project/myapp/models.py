from django.db import models

# Create your models here.
class Form(models.Model):
    username=models.CharField(max_length=50,default="Ano")
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=50)