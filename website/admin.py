from django.contrib import admin
from .models import Product


class PersonAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'store', 'animal', 'category', 'brand',
                    'normal_price', 'sale_price', 'sale', 'age_group')


admin.site.register(Product, PersonAdmin)
