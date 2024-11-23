from django.contrib import admin
from .models import *



@admin.register(CategoriesModel)
class CategoriesAdmin(admin.ModelAdmin):
    pass

