from django.db import models
from django.conf import settings
from api.models import TimestampableMixin

def category_image_path(instance, filename):
    return f"product/category/icons/{instance.name}/{filename}"

def product_image_path(instance, filename):
    return f"product/icons/{instance.name}/{filename}"

def get_default_product_category():
    return ProductCategory.objects.get_or_create(name="Others")[0]

# Model
class ProductCategory(TimestampableMixin):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=category_image_path, blank=True)

    def __str__(self) -> str:
        return self.name

class Product(TimestampableMixin):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name="products", 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=product_image_path, blank=True)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(
        ProductCategory, 
        related_name='product_list',
        on_delete=models.SET(get_default_product_category),
    )
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.seller.username} - {self.name}'