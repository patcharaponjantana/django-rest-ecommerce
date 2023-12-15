from rest_framework import viewsets, permissions
from api.order.models import Order, OrderItem  
from api.order import serializers 

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    # serializer_class = serializers.OrderReadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return serializers.OrderWriteSerializer
        return serializers.OrderReadSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]



