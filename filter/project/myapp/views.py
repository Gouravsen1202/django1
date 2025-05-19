from django.shortcuts import render

# # Create your views here.
def index(request):
     x={'name':'neraj'}
     return render(request,'index.html',x)
