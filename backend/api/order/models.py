from django.db import models
from django.conf import settings
from api.models import TimestampableMixin
from api.product.models import Product

class Order(TimestampableMixin):
    PENDING = 'P'
    COMPLETED = 'C'
    STATUS_CHOICE = (
       (PENDING, 'pending'),
       (COMPLETED, 'completed'),
    )

    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='orders',
        on_delete=models.CASCADE,
    )   
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=PENDING)

    def __str__(self):
        return f'{self.buyer.username} - {self.status}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='order_items',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name='product_orders',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()
