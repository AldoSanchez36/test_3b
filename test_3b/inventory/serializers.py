from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'stock']

class ProductStockUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['stock']