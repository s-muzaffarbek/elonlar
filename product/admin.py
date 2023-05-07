import product.translation
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from product.models import Product, Category


class ProductAdmin(TranslationAdmin):
    list_display = ['name']

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(TranslationAdmin):
    fields = ['name', 'image']

admin.site.register(Category, CategoryAdmin)


