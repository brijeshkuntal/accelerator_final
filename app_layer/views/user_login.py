from rest_framework.views import APIView
from app_layer.command.UserLoginCommand import UserLoginCommand
from app_layer.command.handlers.UserLoginHandler import UserLoginHandler
from mediatr import Mediator


class UserLoginView(APIView):
    """
        This class is used to logged into user account .
        params:
        username- username for user. It must be unique.
        password- password for user.
    """
    def post(self, request, format=None):
        mediator = Mediator()
        command = UserLoginCommand(request)
        result = mediator.send(command)
        return result