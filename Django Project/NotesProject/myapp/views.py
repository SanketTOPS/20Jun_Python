from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=='POST': #root condition
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
                messages.success(request,"Signup Successfully!")
            else:
                print(newuser.errors)
                messages.error(request,newuser.errors)
        elif request.POST.get('signin')=='signin':
            unm=request.POST['username']
            pas=request.POST['password']

            user=usersignup.objects.filter(username=unm,password=pas)
            if user:
                print("Login successfully!")
                messages.success(request,"Login Success!")
                request.session['user']=unm
                return redirect('notes')
            else:
                messages.error(request,"Oops... Login faild....Try again!")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')