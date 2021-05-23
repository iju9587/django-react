from django.db import models


class Weather(models.Model):
    name = models.CharField("Name", max_length=200)
    weather_status = models.CharField("WeatherStatus", max_length=200)
    def __str__(self):
        return self.name
