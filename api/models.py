from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .mixins import BasicUserFieldMixin


class User(BasicUserFieldMixin, AbstractBaseUser, PermissionsMixin):
    """Represents a user in our system"""
    pass


class SavingsGroup(models.Model):
    """Represents a savings group in our system"""
    name = models.CharField(verbose_name=_("Savings Group") ,max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='savings_group', through='UsersSavingsGroup')
    date_created = models.DateTimeField(verbose_name=_('date created'), default=timezone.now, editable=False)

    def __str__(self):
        return self.name


class UsersSavingsGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    savings_group = models.ForeignKey(SavingsGroup, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(verbose_name=_('date joined'), default=timezone.now, editable=False)
