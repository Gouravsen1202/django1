from django.db import models

class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField(max_length=50)
    stu_contact=models.IntegerField(max_length=50)
    stu_city=models.CharField(max_length=50)

    class Meta:
        db_table='Student'
        verbose_name='NewName'
        verbose_name_plural='Student'


        ordering=['id'] # aur isse number me
        ordering=['-stu_name'] # isse apni table alphabat ke hisab se name arrange jayege
