# Generated by Django 2.0.1 on 2018-03-11 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0014_auto_20180311_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weatherinfo',
            options={'ordering': ['-date']},
        ),
    ]
