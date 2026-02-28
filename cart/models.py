from django.db import models
from products.models import *
from django.contrib.auth.models import User



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits = 10, decimal_places = 2,default=None)
    total = models.DecimalField(max_digits = 10, decimal_places = 2, blank=True, default=None)


    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)
