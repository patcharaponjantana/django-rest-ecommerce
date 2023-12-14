from rest_framework import permissions, viewsets
from api.product.models import ProductCategory, Product
from api.product import serializers
from api.product.permissions import IsOwnerOrAdmin

class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = serializers.ProductCategoryReadSerializer
    permission_classes = [permissions.AllowAny]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        print(self.action)
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return serializers.ProductWriteSerializer
        return serializers.ProductReadSerializer
    
    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrAdmin]    
        else:
            self.permission_classes = [permissions.AllowAny]

        return super().get_permissions()