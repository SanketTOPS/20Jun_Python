from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def error(request):
    return render(request,'error.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')