# Generated by Django 4.1.7 on 2023-03-10 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_data_name_data_soilmoisture_data_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='soilmoisture',
        ),
    ]