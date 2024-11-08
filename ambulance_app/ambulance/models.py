from django.db import models

# Create your models here.

class Ambulance(models.Model):
    license_plate = models.CharField(max_length=20)
    current_location = models.CharField(max_length=100)  # Alternatively, use coordinates
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('busy', 'Busy')])
    driver_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

class Request(models.Model):
    requester_name = models.CharField(max_length=100)
    requester_location = models.CharField(max_length=100)
    ambulance = models.ForeignKey(Ambulance, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    timestamp = models.DateTimeField(auto_now_add=True)

