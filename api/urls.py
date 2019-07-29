from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, LoginViewSet,
                    LogoutViewSet, SavingsGroupViewSet, UserSavingsGroupViewSet)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('savings-group', SavingsGroupViewSet)
router.register('users-savings-group', UserSavingsGroupViewSet)
router.register('login', LoginViewSet, base_name='login')
router.register('logout', LogoutViewSet, base_name='logout')

urlpatterns = [
    url('', include(router.urls)),
]
