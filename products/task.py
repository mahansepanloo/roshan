from celery import shared_task
from categories.models import CategoriesModel
import csv
import os
from django.utils import timezone



@shared_task(bind=True, default_retry_delay=5)
def save_top(self):
    try:
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
            print('mahansepanlooghajar')
    except Exception as e:
        return self.retry(exc=e, max_retries=10)
