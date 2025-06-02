from django.db import models
from products.models import *

class Cart(models.Model):
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    total = models.DecimalField(max_digits = 10, decimal_places = 2)



