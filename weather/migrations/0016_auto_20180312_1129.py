# Generated by Django 2.0.1 on 2018-03-12 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0015_auto_20180311_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='cWeather',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='currentWeather', to='weather.WeatherInfo'),
        ),
        migrations.AlterField(
            model_name='city',
            name='img',
            field=models.URLField(),
        ),
    ]
