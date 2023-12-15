from rest_framework import serializers
from api.order.models import Order, OrderItem
from api.product.serializers import ProductReadSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ["order"]

class OrderReadSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

class OrderWriteSerializer(serializers.ModelSerializer):
    buyer = serializers.HiddenField(default=serializers.CurrentUserDefault())    
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ["status"]

    
    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)

        # create order item
        item_list = [ OrderItem(order=order, **item) for item in order_items ]
        OrderItem.objects.bulk_create(item_list)
        return order

