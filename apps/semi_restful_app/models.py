from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    price = models.IntegerField()
