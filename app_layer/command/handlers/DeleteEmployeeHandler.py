from app_layer.command.DeleteEmployeeCommand import DeleteEmployeeCommand
from app_layer.serializers.employee_serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from mediatr import Mediator


@Mediator.handler
class DeleteEmployeeHandler:
    """
    This class handles the task of adding category to organization level
    Table name -- master_categories
    """

    def handle(self, request: DeleteEmployeeCommand):
        request.emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
