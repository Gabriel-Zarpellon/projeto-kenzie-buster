from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ]
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(default=None)
    is_employee = serializers.BooleanField(default=False)
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)
