from rest_framework.views import APIView
from app_layer.command.UserRegistrationCommand import UserRegistrationCommand
from app_layer.command.handlers.UserRegistrationHandler import UserRegistrationHandler
from mediatr import Mediator



class UserRegistrationView(APIView):
    """
    This class is used to register a new user.
    params:
    username- username for user. It must be unique.
    email- email for user.
    display_name- display name for user.
    password- password for user.
    """
    def post(self, request, format=None):
        mediator = Mediator()
        command = UserRegistrationCommand(request)
        return mediator.send(command)