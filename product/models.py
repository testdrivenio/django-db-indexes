from django.db import models


# Create your models here.

class ProductCategory(models.TextChoices):
    ELECTRONICS = "electronics", "Electronics"
    CLOTHING = "clothing", "Clothing"
    HOME_APPLIANCES = "home appliances", "Home Appliances"


class ProductWithoutIndex(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=ProductCategory.choices)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product_without_index"


class ProductWithSingleIndex(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.CharField(max_length=50, db_index=True)
    price = models.IntegerField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product_with_single_index"

    
class ProductWithCompositeIndex(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product_with_composite_index"
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['category', 'price'], name='category_price_idx'),
        ]


