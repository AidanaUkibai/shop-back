from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    is_active = models.BooleanField()


    def __str__(self):
        return f'{self.id} {self.name} {self.quantity}'

class Category(models.Model):

    name1 = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} {self.name1}'

