from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def reg(request):
    if request.method=='POST':
        username=request.POST['username']
        f_name=request.POST['first_name']
        l_name=request.POST['last_name']
        mail_id=request.POST['mailid']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user already exists")
                return redirect('registration')
            if User.objects.filter(email=mail_id):
                messages.info(request,"email already registered")
                return redirect('registration')
            user=User.objects.create_user(username=username,first_name=f_name,last_name=l_name,email=mail_id,password=pass1)
            user.save()
            print(" user saved")
            return redirect('login')
        else:
            messages.info(request,'password mismatch')
            return redirect('registration')
        return redirect('/')
    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    return render(request,"log1.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
