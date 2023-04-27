from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Address
from .serializer import ProductSerializer, AddressSerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer



