from django.shortcuts import render,HttpResponse,redirect
from  .models import Form

# Create your views here.
def form(request):
    if request.method=='POST':
        print(request.method)
        print(request.POST)
        name1=request.POST.get('username')
        email1=request.POST.get('email')
        message1=request.POST.get('message')
        print(name1,email1,message1)
        Form.objects.create(username=name1, email=email1, message=message1)
        
        return render(request,'form.html')

    return render(request,'form.html')
    
def update(request):
    if request.method=='POST':
        record_id=request.POST.get('id')
        name1=request.POST.get('username')
        email1=request.POST.get('email')
        message1=request.POST.get('message')

        obj=Form.objects.filter(id=record_id).first()
        if obj:
            obj.name=name1
            obj.email=email1
            obj.message=message1
            obj.save()
            return redirect('form')
        else:
            return HttpResponse("Record not found")
        
    return HttpResponse("Invalid request")    
