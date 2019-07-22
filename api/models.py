from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .mixins import BasicUserFieldMixin


class User(BasicUserFieldMixin, AbstractBaseUser, PermissionsMixin):
    """Represents a user in our system"""
    pass
