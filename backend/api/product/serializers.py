from rest_framework import serializers
from api.product.models import ProductCategory, Product

class ProductCategoryReadSerializer(serializers.ModelSerializer):
    '''
    Serializer class for reading product category
    '''
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductReadSerializer(serializers.ModelSerializer):
    '''
    Serializer class for reading product
    '''
    class Meta:
        model = Product
        fields = '__all__'

class ProductWriteSerializer(serializers.ModelSerializer):
    '''
    Serializer class for writing product and automatic add/update product category
    '''

    seller = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = ProductCategoryReadSerializer()

    class Meta:
        model = Product
        fields = ['seller', 'category', 'name', 'description', 'image', 'price', 'quantity']

    def create(self, validated_data):
        print(validated_data)
        category = validated_data.pop('category')
        instance, created = ProductCategory.objects.get_or_create(**category)
        product = Product.objects.create(**validated_data, category=instance)

        return product