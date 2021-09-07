from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        ('Custom fields', {'fields': ('profile_picture', 'current_org')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
