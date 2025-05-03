from rest_framework import serializers
from .models import *


class CategoryCSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = ("name", "id")
        read_only_fields = ("id",)

    def validate_name(self, value):
        if CategoriesModel.objects.filter(name=value).exists():
            raise serializers.ValidationError("Category already exists")
        return value


class CategoryESerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = "__all__"
        read_only_fields = ("id",)
        extra_kwargs = {"name": {"required": False}}

    def validate_name(self, value):
        if CategoriesModel.objects.filter(name=value).exists():
            raise serializers.ValidationError("Category already exists")
        return value


class ShowProductCategorySerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = CategoriesModel
        fields = ("name", "product")

    def get_product(self, obj):
        return [item.name for item in obj.product.all()]


class AddProductCategorySerializer(serializers.Serializer):
    product = serializers.IntegerField()
