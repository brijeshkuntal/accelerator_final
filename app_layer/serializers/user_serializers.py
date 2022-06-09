from rest_framework import serializers
from app_layer.models.user_models import CustomUser


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True, max_length=100)
    display_name = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True, max_length=50)
    date_joined = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        try:
            user = CustomUser.objects.create(**validated_data)
            user.set_password(validated_data['password'])
            user.is_active = True
            user.is_superuser = False
            user.save()
            return user
        except Exception as e:
            raise serializers.ValidationError(e)