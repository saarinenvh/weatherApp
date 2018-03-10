from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50);
    lat = models.FloatField()
    lon = models.FloatField()
    slug = models.SlugField(max_length=50);
    cWeather = models.ForeignKey('weatherInfo', on_delete=models.CASCADE, related_name='currentWeather')

class WeatherInfo(models.Model):
    wheater_choices = (('sunny', 'Sunny'), ('rainy', 'Rainy'), ('cloudy', 'Cloudy'), ('misty', 'Misty'))
    city = models.ForeignKey('City', on_delete = models.CASCADE)
    temperature = models.FloatField(validators = [MinValueValidator(-60), MaxValueValidator(60)])
    weather = models.CharField(max_length = 50, choices=wheater_choices, default='sunny')
    comment = models.CharField(max_length=255, blank=True, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
