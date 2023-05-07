from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Address, Product, Category
from .serializer import ProductSerializer, AddressSerializer, CategorySerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

from django.template.response import TemplateResponse
def home():
    return TemplateResponse('index.html')


