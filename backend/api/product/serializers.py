from rest_framework import serializers
from api.product import models

class ProductCategoryReadSerializer(serializers.ModelSerializer):
    '''
    Serializer class for reading product category
    '''
    class Meta:
        model = models.ProductCategory
        fields = '__all__'

class ProductReadSerializer(serializers.ModelSerializer):
    '''
    Serializer class for reading product
    '''
    class Meta:
        model = models.Product
        fields = '__all__'

class ProductWriteSerializer(serializers.ModelSerializer):
    '''
    Serializer class for writing product and automatic add/update product category
    '''
    class Meta:
        model = models.Product
        fields = '__all__'