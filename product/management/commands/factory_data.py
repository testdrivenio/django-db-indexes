import factory
import random

from product.models import (
    ProductWithCompositeIndex,
    ProductWithSingleIndex,
    ProductWithoutIndex,
)


class ProductFactoryMeta(factory.Factory):
    name = factory.Faker("name")
    category = lambda x: x.category
    price = factory.LazyAttribute(lambda _: random.randint(1, 1000))

    class Meta:
        abstract = True

    class Params:
        category = "category1"


class ProductWithoutIndexFactory(
    factory.django.DjangoModelFactory, ProductFactoryMeta
):

    class Meta:
        model = ProductWithoutIndex


class ProductWithSingleIndexFactory(
    factory.django.DjangoModelFactory, ProductFactoryMeta
):

    class Meta:
        model = ProductWithSingleIndex


class ProductWithCompositeIndexFactory(
    factory.django.DjangoModelFactory, ProductFactoryMeta
):

    class Meta:
        model = ProductWithCompositeIndex

