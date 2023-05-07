from modeltranslation.translator import translator, TranslationOptions
from product.models import Address, Category, Product, District

class DistrictTranslationOptions(TranslationOptions):
    model = District
    fields = ('name',)


translator.register(District, DistrictTranslationOptions)

class ProductTranslationOptions(TranslationOptions):
    model = Product
    fields = ('name', 'description')

translator.register(Product, DistrictTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    model = Category
    fields = ('name',)

translator.register(Category, DistrictTranslationOptions)
