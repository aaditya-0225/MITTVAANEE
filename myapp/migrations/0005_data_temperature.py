# Generated by Django 4.1.7 on 2023-03-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_temp_data_moisture'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='temperature',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
