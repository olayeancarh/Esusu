from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .mixins import BasicUserFieldsMixin

# Create your models here.
class User(BasicUserFieldsMixin, PermissionsMixin, AbstractBaseUser):
    """This Class is going to represent a 'user' in our system or any where it is being used. """
    pass
