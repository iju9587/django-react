# Generated by Django 3.0.5 on 2021-05-20 12:09

from django.db import migrations


def create_data(apps, schema_editor):
    Weather = apps.get_model('weather', 'Weather')
    Weather(name="sunny").save()


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
    ]