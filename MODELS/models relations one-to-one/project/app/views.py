from django.shortcuts import render
from .models import Student

def User(request):
    data=Student.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())
    
    data1=Student.objects.get(name='Shubham')
    print(data1.name)
    print(data1.email)
    print(data1.contact)
    print(data1.aadhar)
    print(data1.aadhar.adhar)
    print(data1.aadhar.created_by)
   
 
# Create your views here.
