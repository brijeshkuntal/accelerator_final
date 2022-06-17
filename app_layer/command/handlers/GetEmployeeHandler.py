from app_layer.command.GetEmployeeCommand import GetEmployeeCommand
from app_layer.models import Employee
from app_layer.serializers.employee_serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from mediatr import Mediator


@Mediator.handler
class GetEmployeeHandler:
    """
    This class handles the task of adding category to organization level
    Table name -- master_categories
    """

    def handle(self, request: GetEmployeeCommand):
        emp_obj = Employee.objects.all()
        print(emp_obj)
        emp_list = []
        for obj in emp_obj:
            serializer = EmployeeSerializer(obj)
            emp_list.append(serializer.data)
        return Response(emp_list, status=status.HTTP_200_OK)