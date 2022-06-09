from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_layer.models.user_models import CustomUser
from django.http import Http404
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLoginView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def post(self, request, format=None):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        if not username:
            return Response({
                "message": "Username can not be blank"
            }, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            if not username:
                return Response({
                    "message": "Password can not be blank"
                }, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(username=username, is_superuser=False, is_active=True)
            if not user.check_password(password):
                return Response({
                    "message": "Please enter correct password."
                }, status=status.HTTP_400_BAD_REQUEST)
            token = get_tokens_for_user(user)
            return Response({
                "userName":user.username,
                "displayName":user.display_name,
                **token
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "message": "User doesn't exist"
            }, status=status.HTTP_400_BAD_REQUEST)