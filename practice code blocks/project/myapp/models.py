from django.db import models

# Create your models her

from django.db import models
from datetime import datetime

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    appointment_time = models.DateTimeField(help_text="Enter the appointment date and time.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    default_time = models.DateTimeField(default=datetime.now)
def __set__(self):
    return self.name
