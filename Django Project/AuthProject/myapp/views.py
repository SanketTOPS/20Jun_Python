from django.shortcuts import render,redirect
from .forms import signupForm
from .models import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        fnm=usersignup.objects.get(username=unm)
        print("Name:",fnm.firstname)
        user=usersignup.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login Successfull!")
            request.session["user"]=unm #create a session
            request.session["name"]=fnm.firstname+fnm.lastname #create a session for firstname
            return redirect('home')
        else:
            print("Error!Login Fail...")
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        newuser=signupForm(request.POST)
        if newuser.is_valid():                                                                                                               
            newuser.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def home(request):
    #user=request.session.get('user')
    name=request.session.get('name')
    return render(request,'home.html',{'name':name})


def userlogout(request):
    logout(request)
    return redirect('/')