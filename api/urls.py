
from django.urls import path
from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("employees",views.EmployeeViewSetView,basename="employees")

router.register("tasks",views.TaskViewSetView,basename="tasks")

urlpatterns = [
    
    
]+router.urls