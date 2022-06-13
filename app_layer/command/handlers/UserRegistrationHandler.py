from app_layer.command.UserRegistrationCommand import UserRegistrationCommand
from app_layer.serializers.user_serializers import UserSerializer
from app_layer.models.user_models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from mediatr import Mediator
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    """
    This method is used to verify jwt token for user.
    """
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



@Mediator.handler
class UserRegistrationHandler:
    """
    This class handles the task of adding category to organization level
    Table name -- master_categories
    """

    def handle(self, request: UserRegistrationCommand):
        serializer = UserSerializer(data=request.request.data)
        if serializer.is_valid():
            serializer.save()
            user = CustomUser.objects.get(username=request.request.data["username"], password=serializer.data["password"])
            token = get_tokens_for_user(user)
            return Response({
                "username": user.username,
                "displayName": user.display_name,
                **token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
