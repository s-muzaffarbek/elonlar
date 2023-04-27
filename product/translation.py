from modeltranslation.translator import translator, TranslationOptions
from product.models import Address, Category, Product, District

class DistrictTranslationOptions(TranslationOptions):
    model = District
    fields = ('name',)


translator.register(District, DistrictTranslationOptions)