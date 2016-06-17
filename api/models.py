from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    category = models.ForeignKey(to=Category)
