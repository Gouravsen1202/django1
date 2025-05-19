from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'home.html')
def home(request):
    data={'name':'gourav','age':43}
    return render(request,'home.html',data)