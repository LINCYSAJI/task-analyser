from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from rest_framework.decorators import action


from  rest_framework import viewsets

from api.serializers import EmployeeSerializer,TaskSerializer

from myapp.models import Employee,Task



class EmployeeViewSetView(viewsets.ModelViewSet):
    
    serializer_class=EmployeeSerializer
    
    queryset=Employee.objects.all()
    
    
    #localhost:8000/api/Employee/departments
    
    @action(methods=["GET"],detail=False)
    def departments(self,request,*args, **kwargs):
        
        qs=Employee.objects.all().values_list("department",flat=True).distinct()
        
        return Response(data=qs)
    
    
    #localhost:8000/api/employees/{id}/add_task
    #method:POST
    
    @action(methods=["POST"],detail=True)
    def add_task(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        employee_obj=Employee.objects.get(id=id)
        
        serializer_instance=TaskSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save(employee_object=employee_obj)
            
            return Response(serializer_instance.data)
        
        else:
            
            return Response(serializer_instance.errors)
        
        
# url:locaqlhost:8000/api/tasks/{id}

class TaskViewSetView(viewsets.ModelViewSet):
    
    serializer_class=TaskSerializer
    
    queryset=Task.objects.all()
    
    
    
    