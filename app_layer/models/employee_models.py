from django.db import models
import datetime
from app_layer.behavioural import validators
from .employee_task_models import Task


class Employee(models.Model):
    """
    Employee Model Schema
    """
    empID = models.AutoField(primary_key=True)
    empName = models.CharField(max_length=100, validators=[validators.validate_name])
    empDOJ = models.DateField(auto_now_add=True, validators=[validators.validate_date])
    empDescription = models.CharField(max_length=250, blank=True, validators=[validators.validate_empDescription])
    empCategory = models.CharField(max_length=100, blank=True)
    empCity = models.CharField(max_length=50)
    empOfficeVenue = models.CharField(max_length=500)
    empOrg = models.CharField(max_length=50, blank=True)
    empTask = models.OneToOneField(Task, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.empName
