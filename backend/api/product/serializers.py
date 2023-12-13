from rest_framework import serializers
from api.product import models

class ProductCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = '__all__'