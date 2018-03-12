from django.shortcuts import render
from django import forms
from . import models
from . import forms
import datetime
from django.db.models import Max

# Create your views here.

def index(request):
    citys = models.City.objects.all()
    return render(request, 'index.html', {'citys': citys})

def detail(request, name):
    citys = models.City.objects.all()
    city = models.City.objects.get(name = name)
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    info = models.WeatherInfo.objects.filter(city=city, date__gte = date_from).order_by('-date')
    if request.method == 'POST':
        form = forms.addInfo(request.POST)
        if form.is_valid():
            temperature = form.cleaned_data['temperature']
            weather = form.cleaned_data['weather']
            comment = form.cleaned_data['comment']
            entry = models.WeatherInfo(city = city, temperature = temperature, weather = weather, comment = comment)
            entry.save()
            city.cWeather = entry
            city.save()

    else:
        form = forms.addInfo

    return render(request, 'detail.html', {'info': info, 'city': city, 'form': form, 'citys': citys})
