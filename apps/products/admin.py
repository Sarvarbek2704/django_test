from django.contrib import admin
from apps.products.models import Product, SaleTypeChoices, ProductCategory, ProductImage


admin.site.register(Product)
admin.site.register(SaleTypeChoices)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
