from django.db import models



class ProductsModel(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.PositiveBigIntegerField()
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	views = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ('-available',)

	def save(self, *args, **kwargs):
		if self.stock == 0:
			self.available = False
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.name} - view {self.views}"



class ViewssModel(models.Model):
	userip = models.CharField()
	product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, related_name='viewsss')

	def __str__(self):
		return f"{self.userip}"