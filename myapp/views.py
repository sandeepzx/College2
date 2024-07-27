from django.shortcuts import render,redirect
from .models import Usermember,CustomUser
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def home(req):
    return render(req,'home.html')

def fregister(req):
    return render(req,'reg.html')
def tregister(req):
    return render(req,'tregister.html')
def sregister(req):
    return render(req,'sregister.html')

def register(req):
    if req.method == 'POST':
        fname = req.POST['fname']
        lname = req.POST['lname']
        uname = req.POST['uname']
        email = req.POST['email']
        age = req.POST['age']
        number = req.POST['number']
        image = req.FILES['image']
        passw = req.POST['pass']
        cpass = req.POST['cpass']
        utype = req.POST['utype']
        if passw == cpass:
            if CustomUser.objects.filter(username=uname).exists():
                return redirect('fregister')
            else:
                user = CustomUser.objects.create_user(first_name=fname,last_name = lname,username=uname,password=passw,email=email,user_type=utype)
                user.save()
                member = Usermember(Age=age,Number=number,Image=image,user=user)
                member.save()
            return redirect('home')
    return redirect('fregister')

def ulogin(req):
    if req.method == 'POST':
        uname = req.POST['uname']
        passw = req.POST['pass']
        user = authenticate(username =uname,password=passw)

        if user is not None:
            if user.user_type == '1':
                login(req,user)
                return redirect('adminpage')
            elif user.user_type == '2':
                auth.login(req,user)
                return redirect('teacherpage')
            else:
                auth.login(req,user)
                return redirect('studentpage')
        return redirect('ulogin')
    return render(req,'login.html')

def ulogout(req):
    t = req.user.user_type
    if t=='1':
        logout(req)
    else:
        auth.logout(req)
    print(t)
    return redirect('home')

def adminpage(req):
    return render(req,'admin.html')

def teacherpage(req):
    return render(req,'teacher.html')

def studentpage(req):
    return render(req,'student.html')