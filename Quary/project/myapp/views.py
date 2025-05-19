from django.shortcuts import render
from .models import Student

# Create your views here

def home(request):
    # all_data=Student.objects.all()
    # print(all_data)
    # print(all_data.values())  # for all data dekhne ke liye

    # data=Student.objects.filter(name="ajay",branch="cse")
    # print(data)
    # print(data.values())
    # print(data.values_list())# for  filter

    # data=Student.objects.order_by('name')
    # print(data.values_list()) # for accending order

    # data=Student.objects.order_by('-name')
    # print(data.values_list()) # for decinding order

    data=Student.objects.exclude(name='ajay')
    print(data.values_list()) # for removing that name of object

