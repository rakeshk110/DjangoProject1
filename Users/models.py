from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Role_choice = (
        ('admin','Admin'),
        ('organizer', 'Organizer'),
        ('customer', 'Customer')
    )
    role = models.CharField(max_length=20,choices=Role_choice, default='customer')

    def __str__(self):
        return self.username
