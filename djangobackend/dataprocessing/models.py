
from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=200)

class WindSpeed(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    windspeed = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

class Temperature(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

