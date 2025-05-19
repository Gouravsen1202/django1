from django.shortcuts import render

# Create your views here.
def common(request):
    return render(request,'common.html')
def disables(request):
    return render(request,'disables.html')
def features(request):
    return render(request,'features.html')
def home(request):
    return render(request,'home.html')
def pricing(request):
    return render(request,'pricing.html')
def form(request):
    return render(request,'form.html')
def dataform(request):
    print(request.method)
    print(request.POST)
    print(request.GET)
    print(request.files)