from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model


class UserAdmin(BaseUserAdmin):
    # Your custom admin configurations for the User model
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')


# Register your custom User model with the custom admin configuration
admin.site.register(get_user_model(), UserAdmin)
