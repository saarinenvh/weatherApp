# Generated by Django 2.0.1 on 2018-03-11 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0011_auto_20180311_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherinfo',
            name='img',
        ),
    ]
