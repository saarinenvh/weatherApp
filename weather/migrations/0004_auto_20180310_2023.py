# Generated by Django 2.0.1 on 2018-03-10 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20180310_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='weatherinfo',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='weatherinfo',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='weatherinfo',
            name='name',
        ),
        migrations.AddField(
            model_name='weatherinfo',
            name='city',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='weather.City'),
            preserve_default=False,
        ),
    ]
