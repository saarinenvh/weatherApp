from django.shortcuts import render
from django import forms
from .models import City, WeatherInfo
from . import forms
import datetime
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.utils import timezone
datetime.datetime.now(tz=timezone.utc)

# Create your views here.

def index(request):
    citys = City.objects.all()
    return render(request, 'index.html', {'citys': citys})

def detail(request, pk):
    citys = City.objects.all()

    currentCity = City.objects.get(pk = pk)
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    info = WeatherInfo.objects.filter(city=currentCity, date__gte = date_from).order_by('-date')

    if request.method == 'POST':
        form = forms.addInfo(request.POST)
        if form.is_valid():
            temperature = form.cleaned_data['temperature']
            weather = form.cleaned_data['weather']
            comment = form.cleaned_data['comment']
            entry = models.WeatherInfo(city = city, temperature = temperature, weather = weather, comment = comment, date=datetime.datetime.now(tz=timezone.utc))
            entry.save()
            currentCity.cWeather = entry
            currentCity.save()
    else:
        form = forms.addInfo

    return render(request, 'detail.html', {'info': info, 'city': currentCity, 'form': form, 'citys': citys})
