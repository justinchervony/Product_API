from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    picture = models.CharField(max_length=255, default = 'no picture')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    inventory_quantity = models.IntegerField()