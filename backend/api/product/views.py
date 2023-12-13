from rest_framework import viewsets
from api.product.models import ProductCategory
from api.product.serializers import ProductCategorySerializers

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializers