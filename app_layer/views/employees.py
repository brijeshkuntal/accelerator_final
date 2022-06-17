from app_layer.command.AddEmployeeCommand import AddEmployeeCommand
from app_layer.command.DeleteEmployeeCommand import DeleteEmployeeCommand
from app_layer.command.GetEmployeeCommand import GetEmployeeCommand
from app_layer.command.UpdateEmployeeCommand import UpdateEmployeeCommand
from app_layer.command.handlers.AddEmployeeHandler import AddEmployeeHandler
from app_layer.command.handlers.GetEmployeeHandler import GetEmployeeHandler
from app_layer.command.handlers.UpdateEmployeeHandler import UpdateEmployeeHandler
from app_layer.command.handlers.DeleteEmployeeHandler import DeleteEmployeeHandler
from app_layer.models.employee_models import Employee
from app_layer.serializers.employee_serializers import EmployeeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from mediatr import Mediator
from okta_jwt_verifier import AccessTokenVerifier
import asyncio


async def okta_authentication(token):
    jwt_verifier = AccessTokenVerifier(issuer='https://dev-56353795.okta.com/oauth2/default', audience='api://default')
    await jwt_verifier.verify(token)


def verify_token(request):
    """
    This method is used to verify the token for user.
    """
    JWT_authenticator = JWTAuthentication()
    response = JWT_authenticator.authenticate(request)
    if not response:
        return Response({
            "message": "Token can not be blank."
        }, status=status.HTTP_400_BAD_REQUEST)
    request.user = response[0]


class EmployeeList(APIView):
    """
    This class is used to vreate new employee.
    """
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        token = request.META.get("HTTP_AUTHORIZATION", None)
        if not token:
            return Response({
                "message": "Token can not be null."
            }, status=status.HTTP_400_BAD_REQUEST)
        token = token.split(" ")
        if token[0] == "okta":
            try:
                loop = asyncio.new_event_loop()
                loop.run_until_complete(okta_authentication(token[1]))
            except Exception as e:
                print("e", e)
                return Response({
                    "message": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            verify_token(request)
        mediator = Mediator()
        command = GetEmployeeCommand(request)
        result = mediator.send(command)
        return result

    def post(self, request, format=None):
        token = request.META.get("HTTP_AUTHORIZATION", None)
        if not token:
            return Response({
                "message": "Token can not be null."
            }, status=status.HTTP_400_BAD_REQUEST)
        token = token.split(" ")
        if token[0] == "okta":
            try:
                loop = asyncio.new_event_loop()
                loop.run_until_complete(okta_authentication(token[1]))
            except Exception as e:
                print("e", e)
                return Response({
                    "message": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            verify_token(request)
        mediator = Mediator()
        command = AddEmployeeCommand(request)
        result = mediator.send(command)
        return result


class EmployeeDetail(APIView):
    """
    Retrieve, update or delete a employee instance.
    """
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Employee.objects.get(empID=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        token = request.META.get("HTTP_AUTHORIZATION", None)
        if not token:
            return Response({
                "message": "Token can not be null."
            }, status=status.HTTP_400_BAD_REQUEST)
        token = token.split(" ")
        if token[0] == "okta":
            try:
                loop = asyncio.new_event_loop()
                loop.run_until_complete(okta_authentication(token[1]))
            except Exception as e:
                return Response({
                    "message": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            verify_token(request)
        emp = self.get_object(pk)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        token = request.META.get("HTTP_AUTHORIZATION", None)
        if not token:
            return Response({
                "message": "Token can not be null."
            }, status=status.HTTP_400_BAD_REQUEST)
        token = token.split(" ")
        if token[0] == "okta":
            try:
                loop = asyncio.new_event_loop()
                loop.run_until_complete(okta_authentication(token[1]))
            except Exception as e:
                print("e", e)
                return Response({
                    "message": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            verify_token(request)
        emp = self.get_object(pk)
        mediator = Mediator()
        command = UpdateEmployeeCommand(request, emp)
        result = mediator.send(command)
        return result

    def delete(self, request, pk, format=None):
        token = request.META.get("HTTP_AUTHORIZATION", None)
        if not token:
            return Response({
                "message": "Token can not be null."
            }, status=status.HTTP_400_BAD_REQUEST)
        token = token.split(" ")
        if token[0] == "okta":
            try:
                loop = asyncio.new_event_loop()
                loop.run_until_complete(okta_authentication(token[1]))
            except Exception as e:
                print("e", e)
                return Response({
                    "message": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            verify_token(request)
        emp = self.get_object(pk)
        mediator = Mediator()
        command = DeleteEmployeeCommand(emp)
        result = mediator.send(command)
        return result
