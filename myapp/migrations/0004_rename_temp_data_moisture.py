# Generated by Django 4.1.7 on 2023-03-10 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_data_soilmoisture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='temp',
            new_name='moisture',
        ),
    ]
