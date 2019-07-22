import datetime
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth import get_user_model, login, logout
from django.utils.timezone import now
from .serializers import UserSerializer, LoginSerializer
from .authentication import ExpiringTokenAuthentication

# Create your views here.
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (ExpiringTokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('first_name', 'last_name', 'email')


class LoginViewSet(viewsets.ViewSet):

    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        if not created and token.created < now() - datetime.timedelta(hours=24):
            token.delete()
            token = Token.objects.create(user=user)
            token.created = now()
            token.save()

        userObj = UserSerializer(user).data 
        
        return Response({
            "status": status.HTTP_200_OK, "user": userObj, "access_token": f'Token {token}',
        })


class LogoutViewSet(viewsets.ViewSet):
    authentication_classes = (ExpiringTokenAuthentication,)
    def create(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)