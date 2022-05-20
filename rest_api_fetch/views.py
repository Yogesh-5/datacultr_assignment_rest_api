from django.shortcuts import render
from django.http import JsonResponse
from .models import Model
from .serializers import ModelSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def Model_list(request):
    if request.method == 'GET':
        model = Model.objects.all()
        serializer = ModelSerializer(model,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Modeldetail(request,id):
    try:
        model = Model.objects.get(pk=id)
    except Model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ModelSerializer(model)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ModelSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
