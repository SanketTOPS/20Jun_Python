from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        stdata=studinfo.objects.all()
        serail=studserializers(stdata,many=True)
        return Response(data=serail.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serail=studserializers(stid)
    return Response(data=serail.data,status=status.HTTP_200_OK)


@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serail=studserializers(stid)
        return Response(data=serail.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        stdata=studserializers(data=request.data)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serail=studserializers(stid)
        return Response(data=serail.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        stdata=studserializers(data=request.data,instance=stid)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

