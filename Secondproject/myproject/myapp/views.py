from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
   return HttpResponse ("<h1 style=' color:red'>hello....<h1/>")
def about(request):
   data={'name':True,'age':False,'qua':None}
   return JsonResponse(data)

def index(request):
   return render(request,'index.html')
def new(request):
   return redirect('https://www.google.com') # for any wesite link added