from distutils.log import error
import email
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

def login(request,good=False):
    error = "Cet utilisateur n'existe pas"
    try:
        username = request.POST['username'].__str__()
        password = request.POST['password'].__str__()
        user = authenticate(username=username, password=password)
        if username == '':
            error = 'veillez saisir votre username'
            good = True
            return render(request,"login.html",locals())
        elif password == '':
            error = 'veillez saisir votre password'
            good = True
            return render(request,"login.html",locals())
        elif user is not None:
            return redirect('home')
        else:
            good = True
            return render(request,"login.html",locals())
    except KeyError:
        return render(request,"login.html",locals())
    except Exception as e:
        error=e.__str__()
        good = True
        return render(request,"signin.html",locals())
    
def home(request):
    return render(request,'home.html')


def signin(request,good=False):
    error = 'Je suis une erreur'
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password,email=email)
        if user is not None:
            return redirect('home')
        else:
            good = True
            return render(request,"signin.html",locals())
    except KeyError:
        return render(request,"signin.html",locals())
    except ValueError as e:
        error=e.__str__()
        good = True
        return render(request,"signin.html",locals())