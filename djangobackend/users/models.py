from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser, PermissionsMixin):
    # Add custom fields here if needed
    class Meta:
        pass