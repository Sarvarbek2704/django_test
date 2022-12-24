from rest_framework import serializers
from apps.products.models import Product, ProductCategory, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'image']


class ProductSerializer(serializers.ModelSerializer):
    categories = ProductCategorySerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'images', 'categories', 'price', 'sold', 'sale_type', 'in_stock', 'images']
