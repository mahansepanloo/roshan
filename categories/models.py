from django.db import models
from products.models import ProductsModel


class CategoriesModel(models.Model):
    name = models.CharField(max_length=200)
    product = models.ManyToManyField(ProductsModel, related_name="cproduct", blank=True)

    def __str__(self):
        return self.name
