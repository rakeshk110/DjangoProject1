from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Role_choice = (
        ('admin','Admin'),
        ('organizer', 'Organizer'),
        ('customer', 'Customer')
    )
