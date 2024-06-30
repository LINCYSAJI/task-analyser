from django.db import models


class Employee(models.Model):
    
    name=models.CharField(max_length=200)
    
    department=models.CharField(max_length=200)
    
    salary=models.BigIntegerField()
    
    @property
    def emptask(self):
        
        qs=Task.objects.filter(employee_object=self)
        
        return qs
    
    def __str__(self):
        
        return self.name
    
    
class Task(models.Model):
    
    title=models.CharField(max_length=200)
    
    description=models.CharField(max_length=200)
    
    completion_date=models.DateField(auto_now=True)
    
    assigned_date=models.DateField(auto_now_add=True)
    
    status_choice=(
        ('pending','pending'),
        ('complete','complete')
    )
    
    status=models.CharField(max_length=200,choices=status_choice,default='pending')
    
    employee_object=models.ForeignKey(Employee,on_delete=models.CASCADE)
    
    
    def __str__(self):
        
        return self.title