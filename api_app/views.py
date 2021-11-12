from rest_framework import viewsets

from .models import Employee
from .serializer import employee_serializer


# ----------------Viewsets--------------------------
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employee_serializer


# --------------generics-----------------
# class empview(generics.ListCreateAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employee_serializer
# class empIdview(generics.RetrieveUpdateDestroyAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employee_serializer

# -------------------mixins---------------------------

# class empview(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employee_serializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class empIdview(mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,generics.GenericAPIView):
#
#     queryset = employee.objects.all()
#     serializer_class = employee_serializer
#
#     def get(self,request,pk):
#         return self.retrieve(request)
#
#     def put(self,request,pk):
#         return self.update(request)
#
#     def delete(self,reuqest,pk):
#         return self.destroy(reuqest)

# ----------------APIView------------------
# class empview(APIView):
#     def get(self,request):
#         emp = employee.objects.all()
#         serializer = employee_serializer(emp,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def post(self,request):
#         data = request.data
#         serializer = employee_serializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)
#
# class empIdview(APIView):
#     def get(self,request,id):
#         try:
#             emp = employee.objects.get(id=id)
#         except:
#             emp=None
#             return Response('data not found')
#         else:
#             serializer = employee_serializer(emp)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def emp_id(self,id):
#         try:
#             emp = employee.objects.get(id=id)
#         except:
#             emp=None
#         return emp
#
#     def put(self,request,id):
#         emp = self.emp_id(id=id)
#         if emp is None:
#             return Response('data not found')
#         else:
#             data = request.data
#             serializer = employee_serializer(emp,data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             else:
#                 return Response('data not found')
#
#     def delete(self,request,id):
#         emp = self.emp_id(id= id)
#         if emp is None:
#             return Response('data not found')
#         else:
#             emp.delete()
#             return Response('data delted',status=status.HTTP_204_NO_CONTENT)
