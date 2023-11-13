from django.db import models

# Create your models here.
# users/models.py

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields here if needed
    pass