from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

class Events(AbstractUser):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location =  models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places= 2)
    available_seats = models.PositiveIntegerField()
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Booking(models.Model):
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()
    payment_status = models.CharField(max_length=200, default='pending')
    qr_code = models.ImageField(upload_to='tickets/', blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user.username} - {self.events.title}"