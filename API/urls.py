"""accelerator_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app_layer.views.employees import EmployeeDetail, EmployeeList, get_users, get_task_list, update_employee_task
from django.views.decorators.csrf import csrf_exempt
from app_layer.views.user_register import UserRegistrationView
from app_layer.views.user_login import UserLoginView

# For adding Explorer to GraphiQL IDE
# GraphQLView.graphiql_template = "graphene_graphiql_explorer/graphiql.html"

urlpatterns = [
    path("employees/", get_users),
    path("tasklist/", get_task_list),
    path("update_employee/", update_employee_task),
    path('create_employee/', EmployeeList.as_view()),
    path('register_user/', UserRegistrationView.as_view()),
    path('user_login/', UserLoginView.as_view()),
    path('employee/<int:pk>/', EmployeeDetail.as_view()),
]
