from django.contrib import admin
from api.product import models

admin.site.register(models.ProductCategory)
admin.site.register(models.Product)