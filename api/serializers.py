from rest_framework import serializers

from myapp.models import Employee,Task

class TaskSerializer(serializers.ModelSerializer):
    
    employee_object=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        
        model=Task
        
        fields="__all__"
        
        read_only_fields=["id","assigned_date","completion_date","employee_object","status"]
        

class EmployeeSerializer(serializers.ModelSerializer):
    
    emptask=TaskSerializer(many=True,read_only=True) #nested serilizer
    
    class Meta:
        
        model=Employee
        
        fields=["id","name","department","salary","emptask"]
        





