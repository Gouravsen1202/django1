from django.shortcuts import render
from .models import workers

# Create your views here.


def common(request):
    return render(request, 'common.html')


def login(request):
    return render(request, 'login.html')


def deshbord(request):
    return render(request, 'deshboard.html')


def register(request):
    return render(request, 'register.html')


def registerdata(request):
    print(request.method)
    print(request.POST)
    username = request.POST.get('name')
    email = request.POST.get('email')
    discrips = request.POST.get('detail')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    subscribe = request.POST.getlist('subscribee')
    gender = request.POST.get('gender')
    profile = request.FILES.get('profile-pic')
    resume = request.FILES.get('resume')
    password = request.POST.get('password')
    cpassworde = request.POST.get('cpassword')

    print(username, email, discrips, phone, dob, subscribe,
          gender, profile, resume, password, cpassworde)
    user = workers.objects.filter(email='email')
    if user:
        msg = "user are already exist"
        return render(request, 'login.html', {'msg': msg})
    else:
        if password == cpassworde:
            workers.objects.create(name=username, email=email, discrip=discrips, phone=phone,
                                   dob=dob, subscribe=subscribe, gender=gender, image=profile, resume=resume)
            msg = "registrastion successfully"
            return render(request, 'login.html', {'msg': msg})
        else:
            msg = "pass and cpass dost not a match"
            userdata = {
                'name': username,
                ' email': email,
                'detail': discrips,
                'phone': phone,
                'dob': dob,
                'subscribe': subscribe,
                'gender': gender,
                'profile-pic': profile,
                'resume': resume,
                'password': password,
                'resume': resume
            }
            return render(request, 'register.html', {'msg': msg, 'name': userdata})


def logindata(request):

    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')
        user = workers.objects.filter(email=e)
        if user:
          userdata=workers.objects.get(email=e)
          print(userdata.name)
          print(userdata.email)
          p1 = userdata.password
          if p == p1:
            msg = 'lo ssuus'
            return render(request, 'deshboard.html', {'userdata': userdata,'msg':msg})
          else:
            pmsg = "password does not a match"
            return render(request, 'login.html', {'msg': e})
        else:
          msg = "email does not exits"
          return render(request, 'register.html')
    else:
      return render(request, 'login.html')

