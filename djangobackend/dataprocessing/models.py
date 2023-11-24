
from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=200)

class WindSpeed(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    windspeed = models.FloatField(default=0.0)
    timestamp = models.DateTimeField()

class Temperature(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.FloatField(default=0.0)
    timestamp = models.DateTimeField()

