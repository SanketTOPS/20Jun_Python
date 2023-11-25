from django.shortcuts import render
from .serailization import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        stdata=studinfo.objects.all()
        serial=studSerializers(stdata,many=True)
        return Response(data=serial.data)



