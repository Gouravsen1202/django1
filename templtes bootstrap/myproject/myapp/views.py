from django.shortcuts import render


def home(request):
    return render(request,'home.html')

# Create your views here.

def about(request):
    return render(request,'about.html')
    
def contact(request):
    return render(request,'contact.html')
    
def common(request):
    return render(request,'common.html')
    
def link(request):
    return render(request,'link.html')

def login(request):
    return render(request,'login.html')
