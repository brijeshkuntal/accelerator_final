from django.contrib import admin
from app_layer.models.user_models import CustomUser
from app_layer.models.employee_models import Employee
from app_layer.models.employee_task_models import Task
from multitenant_app.models import Tenant
from django.apps import apps

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Tenant)
admin.site.register(Task)

# app = apps.get_app_config('graphql_auth')

# for model_name, model in app.models.items():
#     admin.site.register(model)
