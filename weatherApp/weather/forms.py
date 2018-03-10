from django import forms
from django.forms import ModelForm
from weather.models import WeatherInfo

class addInfo(ModelForm):
    class Meta:
        model = WeatherInfo
        fields = ['temperature', 'weather', 'comment']
