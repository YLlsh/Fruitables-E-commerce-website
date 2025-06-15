from django.db import models
from products.models import *
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    total = models.DecimalField(max_digits = 10, decimal_places = 2, blank=True, default=0)


    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)
