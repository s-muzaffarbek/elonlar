from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class District(TranslatableModel):
    name = models.CharField()
    longitude = models.FloatField()
    latitude = models.FloatField()

class Region(TranslatableModel):
    name = models.CharField()
    longitude = models.FloatField()
    latitude = models.FloatField()

class Address(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, max_length=256, blank=True)
    street_address_1 = models.CharField(max_length=256, blank=True)
    street_address_2 = models.CharField(max_length=256, blank=True, null=True)
    note = models.CharField(max_length=1024, blank=True)

class Category(TranslatableModel):
    name = models.CharField()
    image = models.ImageField(upload_to='category')
    # subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)

class SubCategory(TranslatableModel):
    name = models.CharField()
    fields = models.ForeignKey('Field', on_delete=models.CASCADE, null=True, blank=True)

class Field(TranslatableModel):
    CHOISE = (
        ("text", "text"),
        ("combobox", "combobox"),
        ("multiselect", "multiselect"),
        ("radio", "radio"),
    )

    name = models.CharField(),
    placeholder = models.CharField(),
    type = models.CharField(choices=CHOISE)
    validation = models.CharField(blank=True, null=True)
    values = models.ForeignKey('Value', on_delete=models.CASCADE, blank=True, null=True)


class Value(TranslatableModel):
    title = models.CharField()

class Product(models.Model):
    name = models.CharField()
    description = models.TextField()
    images = models.ImageField(upload_to='product')
    phones = models.IntegerField(max_length=15)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    type = (
        ("narx", "narx"),
        ("ayirboshlash", "ayirboshlash")
    )
    price_type = (
        ("u.y", "dollar"),
        ("sum", "so'm")
    )
    product_price_type = models.CharField(choices=price_type)
    product_type = models.CharField(choices=type)
    longitude = models.FloatField()
    latitude = models.FloatField()
