from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        """Creates and return a new user"""
        user = User.objects.create_user(
            validated_data['email'],
            validated_data['first_name'],
            validated_data['last_name']
            )

        return user
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}