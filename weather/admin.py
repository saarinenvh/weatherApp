from django.contrib import admin
from . import models

class weatherAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature', 'weather', 'date')

admin.site.register(models.WeatherInfo, weatherAdmin)
admin.site.register(models.City)

# Register your models here.
