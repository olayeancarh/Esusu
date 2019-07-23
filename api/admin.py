from django.contrib import admin
from .models import User, SavingsGroup, UsersSavingsGroup

# Register your models here.
admin.site.register(User)
admin.site.register(SavingsGroup)
admin.site.register(UsersSavingsGroup)