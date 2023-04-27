from rest_framework import serializers
from .models import Product, Address, Category, SubCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Post
        fields = ['title', 'about']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Post
        fields = ['title', 'about']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Post
        fields = ['title', 'about']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Post
        fields = ['title', 'about']

