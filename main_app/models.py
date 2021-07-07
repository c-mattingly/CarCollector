from django.db import models

# Create your models here.
class Car(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    comment = models.TextField(max_length=200)