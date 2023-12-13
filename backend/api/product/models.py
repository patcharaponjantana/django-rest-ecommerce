from django.db import models

# Create your models here.

class TimestampableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

def category_image_path(instance, filename):
    return f"product/category/icons/{instance.name}/{filename}"


class ProductCategory(TimestampableMixin):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=category_image_path, blank=True)
    # icon = models.ImageField(upload_to='img', blank=True)