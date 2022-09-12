from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdmin(UserAdmin):
    ordering = ('-date_joined',)
    list_filter = ('is_active', 'is_superuser', 'first_name', 'last_name')
    list_display = ('mobile', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser')
    list_display_links = ('mobile', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser')
    readonly_fields = ('user_id', 'password', 'last_login', 'date_joined')

    fieldsets = (
        ('Personal Details', {
            'fields': ['user_id', 'email', 'mobile', 'first_name', 'last_name', 'intro']
        }),
        ('Permissions', {
            'fields': ['is_active', 'is_superuser']
        }),
        ('Additional Information', {
            'fields': ['date_joined', 'last_login']
        })
    )

    add_fieldsets = (
        ('Personal Details', {
            'fields': ['user_id', 'email', 'mobile', 'first_name', 'last_name', 'password1', 'password2', 'intro']
        }),
        ('Permissions', {
            'fields': ['is_active', 'is_superuser']
        }),
        ('Additional Information', {
            'fields': ['date_joined', 'last_login']
        })
    )


admin.site.register(User, UserAdmin)
