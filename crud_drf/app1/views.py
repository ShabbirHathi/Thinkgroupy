from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets

from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.all() 

@api_view(['POST'])
def createview(request):
    model=EmployeeModel.objects.get()
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        model.employee_name=request.data['employee_name']
        model.employee_designation=request.data['employee_designation']
        model.contact_number=request.data['contact_number']
        model.save()
        return Response({"status":201,"data":serializer.data,"message":"Added Successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"status":404,"message":"Data is not added"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def readview(request):
    model = EmployeeModel.objects.all()
        
    serializer = EmployeeSerializer(model, many=True)
    # if there is something in items else raise error
    if model:
        return Response({"status":200,"data":serializer.data,"message":""},status=status.HTTP_200_OK)
    else:
        return Response({"status":404,"message":"Data not found!!"},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def updateview(request,pk):
    item = EmployeeModel.objects.get(id=pk)
    data = EmployeeSerializer(instance=item, data=request.data)
    
    if data.is_valid():
        data.save()
        return Response({"status":200,"data":data.data,"message":"Updated Successfully"})
    else:
        return Response({"status":404,"message":"Not Updated, Data is not valid"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteview(request,pk):
    model=EmployeeModel.objects.get(id=pk)
    model.delete()
    return Response({"status":202,"message":"Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
