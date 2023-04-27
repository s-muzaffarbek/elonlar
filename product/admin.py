import product.translation
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from product.models import Product


class ProductAdmin(TranslationAdmin):
    pass



admin.site.register(Product, ProductAdmin)