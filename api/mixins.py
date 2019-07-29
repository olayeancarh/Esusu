from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    """Djando requires user managers to have create_user and create_superuser."""
    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Email address is required'))
        email = self.normalize_email(email).lower()
        user = self.model(
            email=email,
            last_login=timezone.now(),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, email, password, **extra_fields):
        fields = {'is_staff': True, 'is_admin': True,}
        fields.update(extra_fields)
        if not email:
            raise ValueError(_('Email address is required'))
        email = self.normalize_email(email).lower()
        user = self.model(
            email=email,
            last_login=timezone.now(),
            **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def get_by_natural_key(self, email):
        """Get user by email with case-insensitive exact match.

        `get_by_natural_key` is used to `authenticate` a user, see:
        https://github.com/django/django/blob/c5780adeecfbd85a80b5aa7130dd86e78b23e497/django/contrib/auth/backends.py#L16
        """
        return self.get(email__iexact=email)


@python_2_unicode_compatible
class NameUserMethodsMixin:
    def get_full_name(self):
        """Used to get full name of the user"""
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """Used to get short name of the user, firstname is retured here"""
        return self.first_name

    def __str__(self):
        """Django uses this to convert the model object to a string"""
        return self.first_name


class NameUserMixin(NameUserMethodsMixin, models.Model):
    first_name = models.CharField(verbose_name=_('First Name'), max_length=255)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=255)

    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        abstract = True
        ordering = ['first_name', 'last_name']


class PhoneUserMixin(models.Model):
    telephone = models.CharField(verbose_name=_('Phone number'), unique=True,max_length=20)

    class Meta:
        abstract = True


class EmailUserMixin(models.Model):
    email = models.EmailField(verbose_name=_('Email address'), unique=True, max_length=255,)
    email_verified = True

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        abstract = True


class DateJoinedUserMixin(models.Model):
    date_joined = models.DateTimeField(verbose_name=_('date joined'), default=timezone.now, editable=False)

    class Meta:
        abstract = True


class IsStaffUserMixin(models.Model):
    is_staff = models.BooleanField(_('staff status'), default=True)

    class Meta:
        abstract = True


class ActiveUserMixin(models.Model):
    is_active = models.BooleanField('active', default=True)

    class Meta:
        abstract = True


class AvatarMixin(models.Model):
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        abstract = True


class BasicUserFieldMixin(NameUserMixin, EmailUserMixin, PhoneUserMixin, DateJoinedUserMixin, ActiveUserMixin, IsStaffUserMixin):
    class Meta:
        abstract = True