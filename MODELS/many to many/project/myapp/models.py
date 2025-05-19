from django.db import models

# Create your models here.
class Fuel(models.Model):
    Fuel_name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.Fuel_name

class Vicals(models.Model):
    Vicals_name=models.CharField(max_length=50,unique=True)
    Fuel_name=models.ManyToManyField(Fuel,related_name='vicals')
    def __str__(self):
        return self.Vicals_name



