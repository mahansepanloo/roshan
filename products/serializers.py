from rest_framework import serializers
from .models import *



class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductsModel
		fields = '__all__'
		read_only_fields = ('created', 'updated',"views")

	def validate_name(self, value):
		if ProductsModel.objects.filter(name=value).exists():
			raise serializers.ValidationError("Product with this name already exists")
		return value

class ProductSerializer2(serializers.ModelSerializer):
	class Meta:
		model = ProductsModel
		fields = "__all__"
		extra_kwargs = {
			'name':{"required":False},
			"category":{"required":False},
			"description":{"required":False},
			"price":{"required":False},
			"stock":{"required":False},
			"available":{"required":False},
			"views":{"required":False}
		}


