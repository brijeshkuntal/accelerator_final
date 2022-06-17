from app_layer.command.AddEmployeeCommand import AddEmployeeCommand
from app_layer.serializers.employee_serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from mediatr import Mediator


@Mediator.handler
class AddEmployeeHandler:
    """
    This class handles the task of adding category to organization level
    Table name -- master_categories
    """

    def handle(self, request: AddEmployeeCommand):
        serializer = EmployeeSerializer(data=request.request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
