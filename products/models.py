from django.db import models


class Vegetables(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vegetable_images/')
    quantity = models.IntegerField(default = 0)


    def __str__(self):
        return self.product_name
    


class Fruits(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Fruit_images/')
    quantity = models.IntegerField(default = 0)
    def __str__(self):
        return self.product_name