from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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
                uid=usersignup.objects.get(username=unm)
                print("UserID:",uid.id)
                request.session['user']=unm
                request.session['userid']=uid.id
                return redirect('notes')
            else:
                messages.error(request,"Oops... Login faild....Try again!")
    return render(request,'index.html')

#@login_required(login_url='/')
def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})


def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    cuser=usersignup.objects.get(id=userid)
    if request.method=='POST':
        updateprofile=updateForm(request.POST)
        if updateprofile.is_valid():
            updateprofile=updateForm(request.POST,instance=cuser)
            updateprofile.save()
            print("Your profile has been updated!")
            return redirect('notes')
        else:
            print(updateprofile.errors)
    return render(request,'profile.html',{'user':user,'cuser':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect("/")