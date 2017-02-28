from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
  category = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  num_left = models.IntegerField()
  image = models.CharField(max_length=200)
