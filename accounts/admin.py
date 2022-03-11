from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import BaseAccount


@admin.register(BaseAccount)
class BaseAccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    add_fieldsets = (
        (
            "Login Info", {
                'fields': ('email', 'password1', "password2")
            }
        ),
        (
            "Basic Info",
            {
                'classes': ('wide',),
                "fields": ['first_name', 'last_name'],
            },
        )
    )
    fieldsets = (
        (
            "Login Info", {
                'fields': ('id', 'email', 'password')
            }
        ),
        (
            'Personal info', {
                'fields': ('first_name', 'last_name','contact_no')
            }
        ),
        (
            'Permissions', {
                'fields': ('is_superuser', 'is_staff', 'is_active')
            }
        ),
        (
            'Date & Time Info', {
                "fields": ['date_joined', 'last_login'],
            }
        ),
        (
            'Group Permissions', {
                'fields': ('groups', 'user_permissions', ),
            }
        )
    )
    readonly_fields = ('id', 'date_joined',)
    ordering = ('email',)
    list_display = ['email', 'first_name',
                    'last_name', 'is_superuser', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']


