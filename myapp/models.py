from django.db import models

# Create your models here.
class data(models.Model):
    moisture=models.CharField(max_length=5)
    temperature=models.CharField(max_length=5)
