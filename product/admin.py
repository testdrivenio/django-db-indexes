from django.contrib import admin

# Register your models here.
from .models import (
    ProductWithCompositeIndex,
    ProductWithSingleIndex,
    ProductWithoutIndex,
)

admin.site.register(ProductWithCompositeIndex)
admin.site.register(ProductWithoutIndex)
admin.site.register(ProductWithSingleIndex)
