from django.contrib import admin
from .models import *


@admin.register(ProductsModel)
class ProductsAdmin(admin.ModelAdmin):
    pass