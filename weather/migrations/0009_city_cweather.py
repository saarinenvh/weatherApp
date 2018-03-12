# Generated by Django 2.0.1 on 2018-03-10 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0008_auto_20180310_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='cWeather',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currentWeather', to='weather.WeatherInfo'),
            preserve_default=False,
        ),
    ]