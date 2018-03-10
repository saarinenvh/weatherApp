from django.contrib import admin
from . import models

admin.site.register(models.WeatherInfo)
admin.site.register(models.City)

# Register your models here.
