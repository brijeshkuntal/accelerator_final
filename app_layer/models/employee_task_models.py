from django.db import models
import datetime
from app_layer.behavioural import validators


class Task(models.Model):
    """
    Employee Model Schema
    """
    taskID = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=100)
    taskCreatedOn = models.DateField(auto_now_add=True)
    taskDescription = models.CharField(max_length=250, blank=True)
    taskOrg = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.taskName
