from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=100) #Stock Keeping Unit posible agregar ", unique=True"
    name = models.CharField(max_length=250)
    stock = models.IntegerField(default=100)

    def __str__(self):
        return self.name