from django.shortcuts import render
from .models import Fuel,Vicals
 

# Create your views here.
def vicals(req):
    data= Vicals.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())
    details=Vicals.objects.get(id=1)
    print(details.Vicals_name)
    x=details.Fuel_name.all()
    for i in x:
        print(i.Fuel_name)
def fuel(req):
    data=Fuel.objects.all()
    print(data)
    print(data.values())
    print(data.values_list())
    fuel_data=Fuel.objects.get(id=1)
    x=fuel_data.vehical.all()
    for i in x:
        print(i)



