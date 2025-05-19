from django.shortcuts import render
from .models import  Appointment

# Create your views here.
def common(request):
    
    return render(request,"common.html")

