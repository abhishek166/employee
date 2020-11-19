from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.

class EmployeeList(APIView):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):

    def get_object(self,id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request,id,*args,**kwargs):
        qs = self.get_object(id=id)
        serializer = EmployeeSerializer(qs)
        return Response(serializer.data)

    def put(self,request,id,*args,**kwargs):
        qs = self.get_object(id=id)
        serializer = EmployeeSerializer(qs,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,*args,**kwargs):
        qs = self.get_object(id=id)
        qs.delete()
        msg = {"msg": "Resource Deleted Successfully"}
        return Response(msg,status=status.HTTP_204_NO_CONTENT)
