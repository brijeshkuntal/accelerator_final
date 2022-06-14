from app_layer.models.employee_models import Employee
from app_layer.models.employee_task_models import Task
from app_layer.serializers.employee_serializers import EmployeeSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
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
        try:
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
            emp_obj = Employee.objects.all()
            emp_list = []
            for obj in emp_obj:
                serializer = EmployeeSerializer(obj)
                emp_list.append(serializer.data)
            return Response(emp_list, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        try:
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
            serializer = EmployeeSerializer(data=request.data)
            try:
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

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
        try:
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
            data = {
                "empName": emp.empName,
                "empDOJ": emp.empDOJ,
                "empID": emp.empID,
                "empDescription":emp.empDescription,
                "empCategory":emp.empCategory,
                "empCity":emp.empCity,
                "empOfficeVenue":emp.empOfficeVenue
            }
            #serializer = EmployeeSerializer(emp)
            return Response(data)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
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
            serializer = EmployeeSerializer(emp, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
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
            emp.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_users(request):
#     '''
#     This method accept only get request. And
#     it provides the list of employees.
#     '''
#     print(request)
#     verify_token(request)
#     emp_obj = Employee.objects.all()
#     emp_list = []
#     for obj in emp_obj:
#         data = {
#             "empName": obj.empName,
#             "empDOJ": obj.empDOJ,
#             "empID": obj.empID,
#             "empDescription":obj.empDescription,
#             "empCategory":obj.empCategory,
#             "empCity":obj.empCity,
#             "empOfficeVenue":obj.empOfficeVenue
#         }
#         # serializer = EmployeeSerializer(obj)
#         emp_list.append(data)
#     return Response(emp_list,status=status.HTTP_200_OK)
#
# @api_view(['GET'])
# def get_task_list(request):
#     verify_token(request)
#     tenant = request.tenant
#     emp_task = Task.objects.filter(taskOrg=tenant.name, is_active=True)
#     emp_list = []
#     if emp_task:
#         for obj in emp_task:
#             try:
#                 data = {
#                     "taskID": obj.taskID,
#                     "taskName": obj.taskName,
#                     "taskDescription": obj.taskDescription,
#                     "taskOrg": obj.taskOrg,
#                     "task_user": obj.employee.empID
#                 }
#             except:
#                 data = {
#                     "taskID": obj.taskID,
#                     "taskName": obj.taskName,
#                     "taskDescription": obj.taskDescription,
#                     "taskOrg": obj.taskOrg,
#                     "task_user": None
#                 }
#             emp_list.append(data)
#     return Response({"data": emp_list}, status=status.HTTP_200_OK)
#
# @api_view(['PUT'])
# def update_employee_task(request):
#     verify_token(request)
#     tenant = request.tenant
#     task_id = request.data.get("task_id", None)
#     emp_id = request.data.get("emp_id", None)
#     if not emp_id:
#         return Response({"message": "employee not found."}, status=status.HTTP_400_BAD_REQUEST)
#     emp_task = None
#     try:
#         if task_id:
#             emp_task = Task.objects.get(taskOrg=tenant.name, is_active=True, taskID=task_id)
#     except Exception:
#         return Response({"message": "task not found."}, status=status.HTTP_400_BAD_REQUEST)
#     emp_obj = Employee.objects.get(empOrg=tenant.name, empID=emp_id)
#     emp_obj.empTask_id = emp_task.taskID if emp_task else None
#     emp_obj.save()
#     return Response({"message": "data successfully updated."}, status=status.HTTP_200_OK)