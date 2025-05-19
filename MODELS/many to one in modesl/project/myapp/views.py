from django.shortcuts import render
from .models import student,Derparment

# Create your views here.
def Student(request):
    data=student.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    Stu_data= student.objects.get(stu_name="vikas")
    print(Stu_data.stu_name)
    print(Stu_data.stu_email)

    x=Stu_data.stu_dep
    print(x.dep_name)
    print(x.dep_des)

def department(request):
    data=Derparment.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())

    dep_data=Derparment.objects.get(id=1)
    print(dep_data.dep_name)
    print(dep_data.dep_des)
    
  
    



