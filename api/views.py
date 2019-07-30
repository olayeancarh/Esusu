import datetime
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth import get_user_model, login, logout
from django.utils.timezone import now
from .permissions import IsCreationOrIsAuthenticated
from .serializers import UserSerializer, LoginSerializer, SavingsGroupSerializer, UsersSavingsGroupSerializer
from .authentication import ExpiringTokenAuthentication
from .models import SavingsGroup, UsersSavingsGroup

# Create your views here.
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (ExpiringTokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsCreationOrIsAuthenticated,)
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

        user_obj = UserSerializer(user).data 
        
        return Response({
            "status": status.HTTP_200_OK, "user": user_obj, "access_token": f'Token {token}',
        })


class LogoutViewSet(viewsets.ViewSet):
    authentication_classes = (ExpiringTokenAuthentication,)
    def create(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SavingsGroupViewSet(viewsets.ModelViewSet):
    queryset = SavingsGroup.objects.all()
    serializer_class = SavingsGroupSerializer
    authentication_classes = (ExpiringTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        savings_grp_obj = serializer.save() 
        if(savings_grp_obj):
            user_id = savings_grp_obj.owner
            savings_grp_id = savings_grp_obj.id
            savings_grp_obj.userssavingsgroup_set.create(user=user_id,savings_group=savings_grp_id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UsersSavingsGroupSerializer(instance.userssavingsgroup_set.all(), many=True)
        return Response(serializer.data)

class UserSavingsGroupViewSet(viewsets.ModelViewSet):
    queryset = UsersSavingsGroup.objects.all()
    serializer_class = UsersSavingsGroupSerializer
    authentication_classes = (ExpiringTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, list):
            serializer = self.serializer_class(data=request.data, many=True)
        else:
            serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
