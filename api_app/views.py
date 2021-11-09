from django.shortcuts import render
from .models import employee
from .serializer import employee_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class empview(APIView):
    def get(self,request):
        emp = employee.objects.all()
        serializer = employee_serializer(emp,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        serializer = employee_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class empIdview(APIView):
    def get(self,request,id):
        try:
            emp = employee.objects.get(id=id)
        except:
            emp=None
            return Response('data not found')
        else:
            serializer = employee_serializer(emp)
            return Response(serializer.data,status=status.HTTP_200_OK)

    def emp_id(self,id):
        try:
            emp = employee.objects.get(id=id)
        except:
            emp=None
        return emp

    def put(self,request,id):
        emp = self.emp_id(id=id)
        if emp is None:
            return Response('data not found')
        else:
            data = request.data
            serializer = employee_serializer(emp,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response('data not found')

    def delete(self,request,id):
        emp = self.emp_id(id= id)
        if emp is None:
            return Response('data not found')
        else:
            emp.delete()
            return Response('data delted',status=status.HTTP_204_NO_CONTENT)


