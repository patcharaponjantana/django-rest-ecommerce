from django.contrib import admin
from api.product import models

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
