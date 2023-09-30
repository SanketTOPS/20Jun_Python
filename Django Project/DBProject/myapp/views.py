from django.shortcuts import render,redirect
from .forms import studForm,updateForm
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

def updatedata(request,id):
    stid=studinfo.objects.get(id=id)
    if request.method=='POST':
        updatedata=updateForm(request.POST,instance=stid)
        if updatedata.is_valid():
            updatedata.save()
            print("Record updated!")
            return redirect('showdata')
        else:
            print(updatedata.errors)
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect('showdata')
    