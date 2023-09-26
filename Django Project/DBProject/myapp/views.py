from django.shortcuts import render
from .forms import studForm

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