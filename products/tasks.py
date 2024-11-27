from celery import shared_task
from categories.models import CategoriesModel
import csv
import os
from django.utils import timezone
from .models import ProductsModel






from celery import shared_task  

@shared_task  
def my_task():  
        categories = CategoriesModel.objects.all()
        filename = f'top_products_{timezone.now().strftime("%Y%m%d_%H%M")}.csv'
        filepath = os.path.join('media/', filename)
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['محصول', 'دسته بندی', 'تعداد بازدید'])
            for category in categories:
                top_products = category.product.order_by('-views')[:1]
                for product in top_products:
                    writer.writerow([category.name, product.name, product.views])
