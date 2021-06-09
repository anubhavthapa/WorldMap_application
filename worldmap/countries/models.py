from django.db import models
# Create your models here.
from django.shortcuts import render
from django.db import models
from django.utils import timezone


class Countrydata(models.Model):
    name = models.CharField(max_length=128,unique=True)
    geojson = models.JSONField()
    added_date = models.DateTimeField(default=timezone.now,blank=True)
