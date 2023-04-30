from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Address, Product
from .serializer import ProductSerializer, AddressSerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

from django.template.response import TemplateResponse
def home():
    return TemplateResponse('index.html')


