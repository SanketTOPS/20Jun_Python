from django.shortcuts import render
from .forms import studForm
from .models import *

# Create your views here.

def index(request):
    if request.method=='POST':
        stdata=studForm(request.POST)
        if stdata.is_valid(): #true
            stdata.save()
            print("Data saved successfully!")
        else:
            print(stdata.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def updatedata(request):
    return render(request,'updatedata.html')