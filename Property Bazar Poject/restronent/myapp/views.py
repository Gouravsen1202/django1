from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Bazzar,Querys

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def common(request):
    return render(request,'myapp/common.html')

def menu(request):#selling
    return render(request,'myapp/selling.html')

def order(request):#purchase
    return render(request,'myapp/purchase.html')

def trackorder(request):
    return render(request,'myapp/track.html')
def Service(request):
    return render(request,'myapp/Service.html')

# for login data 

def ragister(request):
    if request.method=='POST':
        print(request.method)
        print(request.POST)
           
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        urseimage=request.FILES.get('profile_pic')
        print(name, email, phone, dob, state, gender, password, cpassword,urseimage)
        user = Bazzar.objects.filter(emp_email=email)
        if user:
            msg = "Already have an account"
            return render(request, 'myapp/Ragister.html', {'msg': msg})
        else:
            if password == cpassword:
                Bazzar.objects.create(emp_name=name,emp_email=email,emp_contact=phone,emp_dob=dob,emp_state=state,emp_gender=gender,emp_password=password,emp_profile=urseimage)
                msg = "Registration successful"
                return render(request, 'myapp/login.html', {'msg': msg})
            else:
                msg = "Password and Confirm Password do not match"
                userdata = {
                    'username': name,
                    'email': email,
                    'phone': phone,
                    'dob': dob,
                    'state': state,
                    'gender': gender
                }
                return render(request, 'myapp/Ragister.html', {'msg': msg, 'data': userdata})
    else:
        return render(request, 'myapp/Ragister.html')    
    
    # login form filiig process
def login(request):
    if request.method=='POST':
       e=request.POST.get('email')
       p=request.POST.get('password')
       user=Bazzar.objects.filter(emp_email=e)

       if user:
           userdata=Bazzar.objects.get(emp_email=e)
           print(userdata.emp_name)
           print(userdata.emp_email)
           p1=userdata.emp_password
           if p==p1:
               msg="login succcessfuly"
               return render(request,'myapp/deshbord.html',{'userdata':userdata,'msg':msg,'msg_type': 'success'})
           else:
               msg="password not match"
               return render(request,'myapp/login.html',{'email':e})
       else:
             msg="email does not exist"
             return render(request,'myapp/ragister.html')
       
    else:
        return render(request,'myapp/login.html')

def home1(request,pk):
    userdata=Bazzar.objects.get(id=pk)
    return render(request,'myapp/home.html',{'userdata':userdata})

def menu1(request,pk):
    userdata=Bazzar.objects.get(id=pk)
    return render(request,'myapp/selling.html',{'userdata':userdata})

def order1(request,pk):
    userdata=Bazzar.objects.get(id=pk)
    return render(request,'myapp/purchase.html',{'userdata':userdata})

def trackorder1(request,pk):
    userdata=Bazzar.objects.get(id=pk)
    return render(request,'myapp/track.html',{'userdata':userdata})

def Service1(request,pk):
    userdata=Bazzar.objects.get(id=pk)
    return render(request,'myapp/Service.html',{'userdata':userdata})

def dashboard(request, pk):
    userdata = Bazzar.objects.get(id=pk)
    page = request.GET.get('page', 'dashboard')  # default 'dashboard'

    if page == 'query':
        return render(request, 'myapp/deshbord.html', {
            'userdata': userdata,
            'page_type': 'query',
        })

    elif page == 'allquery':
        querydetails = Querys.objects.filter(stu_email=userdata.emp_email)
        return render(request, 'myapp/deshbord.html', {
            'userdata': userdata,
            'page_type': 'allquery',
            'querydetails': querydetails,
        })

    return render(request, 'myapp/deshbord.html', {
        'userdata': userdata,
        'page_type': 'dashboard',
    })



# for query section ...........
def query(request,pk):
    print(pk)
    userdata=Bazzar.objects.get(id=pk)
    print(userdata)
    print(request.method)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        Querys.objects.create(stu_name=name,stu_email=email,stu_query=query)
        messages.success(request, "Your query has been submitted successfully!")
        
        querydetails=Querys.objects.filter(stu_email=userdata.emp_email)
        
        return render(request,'myapp/deshbord.html',{'userdata':userdata,'querydetails':querydetails,'query':userdata})
    else:
        return render(request,'myapp/deshbord.html',{'userdata':userdata,'query':userdata})
    
def allquery(request,pk):
    userdata=Bazzar.objects.get(id=pk)
    x=userdata.emp_email
    querydetails=Querys.objects.filter(stu_email=x)
    return render(request,'myapp/deshbord.html',{'userdata':userdata,'querydetails':querydetails})

def edit(request, pk):
    editdata = Querys.objects.get(id=pk)
    userdata = Bazzar.objects.get(emp_email=editdata.stu_email)

    if request.method == "POST":
        editdata.stu_query = request.POST['query']
        editdata.save()
        return redirect('deshbord', pk=userdata.id)

    return render(request, 'myapp/deshbord.html', {
        'userdata': userdata,
        'editdata': editdata,
        'page_type': 'edit'
    })
def qupdate(request, pk):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        old_query=Querys.objects.get(id=pk)
        old_query.stu_name=name
        old_query.stu_email=email
        old_query.stu_query=query
        old_query.save()
        querydetails=Querys.objects.filter(stu_email=email)
        userdata=Bazzar.objects.get(emp_email=email)
        return render(request,'myapp/deshbord.html',{'userdata':userdata,'querydetails':querydetails})


def delete(request,pk):
    deletedata=Querys.objects.get(id=pk)
    email=deletedata.stu_email
    deletedata.delete()
    querydetails=Querys.objects.filter(stu_email=email)
    userdata=Bazzar.objects.get(emp_email=email)
    return render(request,'myapp/deshbord.html',{'userdata':userdata,'querydetails':querydetails})
    


def logout(request):
    return render(request,'myapp/login.html')

def contact_view(request):
    return render(request, 'myapp/contact.html')
   


