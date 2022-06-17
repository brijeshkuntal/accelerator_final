from app_layer.command.UpdateEmployeeCommand import UpdateEmployeeCommand
from app_layer.serializers.employee_serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from mediatr import Mediator


@Mediator.handler
class UpdateEmployeeHandler:
    """
    This class handles the task of adding category to organization level
    Table name -- master_categories
    """

    def handle(self, request: UpdateEmployeeCommand):
        serializer = EmployeeSerializer(request.emp, data=request.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
