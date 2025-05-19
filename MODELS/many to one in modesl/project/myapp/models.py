from django.db import models

# Create your models here.
class Derparment(models.Model):
    dep_name=models.CharField(max_length=50,unique=True)
    dep_des=models.TextField(max_length=30)

class student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_dep=models.ForeignKey(Derparment,on_delete=models.PROTECT,to_field='dep_name',related_name='depart')
