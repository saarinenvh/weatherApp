# Generated by Django 2.0.1 on 2018-03-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0009_city_cweather'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherinfo',
            name='img',
            field=models.ImageField(default=0, upload_to='static/img'),
            preserve_default=False,
        ),
    ]