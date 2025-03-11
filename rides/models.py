from django.db import models
from django.contrib.auth.models import User  # Use Django’s built-in User model

class Ride(models.Model):
    driver = models.ForeignKey(User, related_name='drives', on_delete=models.CASCADE, null=True, blank=True)
    passenger = models.ForeignKey(User, related_name='rides', on_delete=models.CASCADE)
    
    # Store Latitude & Longitude from OpenStreetMap
    pickup_lat = models.FloatField(default=0.0)
    pickup_lng = models.FloatField(default=0.0)
    dropoff_lat = models.FloatField(default=0.0)
    dropoff_lng = models.FloatField(default=0.0)


    ride_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('ongoing', 'Ongoing'),
            ('completed', 'Completed')
        ],
        default='pending'
    )

    def __str__(self):
        return f"Ride {self.id}: {self.passenger.username} to ({self.dropoff_lat}, {self.dropoff_lng})"
