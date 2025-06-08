from django.db import models

# Create your models here.


class checkOut(models.Model):
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    total = models.DecimalField(max_digits = 10, decimal_places = 2, blank=True, default=0)

