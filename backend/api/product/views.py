from rest_framework import permissions, viewsets
from api.product.models import ProductCategory, Product
from api.product import serializers

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = serializers.ProductCategoryReadSerializer
    permission_classes = (permissions.AllowAny)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return serializers.ProductReadSerializer
        return serializers.ProductWriteSerializer
    
    