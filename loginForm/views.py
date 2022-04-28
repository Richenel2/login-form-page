import email
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate

# Create your views here.

def login(request,good=False):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('home')
        else:
            good = True
            return render(request,"login.html",locals())
    except KeyError:
        return render(request,"login.html",locals())
    
def home(request):
    return render(request,'home.html')


def signin(request,good=False):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('home')
        else:
            good = True
            return render(request,"signin.html",locals())
    except KeyError:
        return render(request,"signin.html",locals())