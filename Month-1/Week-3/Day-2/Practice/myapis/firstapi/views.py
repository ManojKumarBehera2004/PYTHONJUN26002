from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def welcome(request):
    return Response({'Welcome to the apis'})

@api_view(['POST'])
def postmethod(request):
    
    return Response({"This is a post method"})

@api_view(['GET', 'POST'])
def getorpost(request):

    if request.method == 'GET':
        return Response({"This is a get method, let's post something...."})
    elif request.method == 'POST':
        return Response({"This is a post method, let's get some data from db...."})
    else:
        return Response({"Invalid method"})

    return Response({request.method})