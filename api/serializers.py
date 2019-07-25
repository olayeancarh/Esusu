from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions
from django.utils.translation import ugettext_lazy as _
from .models import SavingsGroup, UsersSavingsGroup

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """A serializer for our user objects"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'telephone', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            """Creates and return a new user"""
            user = User(
                email=validated_data['email'], 
                telephone=validated_data['telephone'], 
                first_name=validated_data['first_name'], 
                last_name=validated_data['last_name'],
                )

            user.set_password(validated_data['password'])

            user.save()

            return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False 
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class SavingsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGroup
        fields = ('name', 'owner', 'members',)


class UsersSavingsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersSavingsGroup
        fields = ('user', 'savings_group',)