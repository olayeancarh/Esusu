from django.contrib import admin
from .models import User, SavingsGroup, UsersSavingsGroup

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'telephone')
    list_display_link = ('email')

class SavingsGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



admin.site.register(User, UserAdmin)
admin.site.register(SavingsGroup, SavingsGroupAdmin)
admin.site.register(UsersSavingsGroup)