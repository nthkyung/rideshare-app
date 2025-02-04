from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_driver = models.BooleanField(default=False)

class Ride(models.Model):
    driver = models.ForeignKey(User, related_name='drives', on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, related_name='rides', on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    ride_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('ongoing', 'Ongoing'), ('completed', 'Completed')])
